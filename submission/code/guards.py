"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _valid_approval(ctx, approval_id: str | None, order: dict, amount_vnd: int) -> bool:
    if not approval_id:
        return False
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    app = rows[0]
    if app.get("status") != "valid":
        return False
    if app.get("expires_at") and app["expires_at"] < ctx.as_of:
        return False
    if app.get("order_id") != order["order_id"] or app.get("customer_id") != order["customer_id"]:
        return False
    if amount_vnd > app.get("max_vnd", 0):
        return False
    if ctx.tools.ledger_rows(approval_id=approval_id):
        return False
    return True


def pre_guard(ctx):
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    order_id = action.get("order_id") or ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)

    if tool == "issue_refund":
        if order is None or pol is None:
            return Verdict.escalate("thiếu đơn hàng hoặc chính sách hiệu lực trong nguồn sự thật")
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            ctx.log("guard_dup_refund", order_id=order["order_id"], ticket_id=ctx.ticket.get("ticket_id"))
            return Verdict.deny("đơn hàng đã có giao dịch hoàn tiền trong sổ cái")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        entitled = H.entitlement_vnd(pol, order, db_delay, parcel.get("delay_cause"))
        if entitled <= 0:
            ctx.log("guard_ineligible_refund", order_id=order["order_id"], db_delay=db_delay,
                    cause=parcel.get("delay_cause"))
            return Verdict.deny("theo tracking DB và chính sách hiệu lực, đơn chưa đủ điều kiện hoàn tiền")

        aid = action.get("approval_id")
        if entitled > pol["auto_limit_vnd"] and not _valid_approval(ctx, aid, order, entitled):
            return Verdict.escalate("vượt hạn mức tự động và thiếu phê duyệt hợp lệ")

        if entitled <= pol["auto_limit_vnd"]:
            cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
            cust_today = sum(
                r["amount_vnd"]
                for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                if not r.get("approval_id")
            )
            if cust_cap is not None and cust_today + entitled > cust_cap:
                return Verdict.escalate("vượt trần hoàn tự động mỗi khách trong ngày")

        if (
            action.get("amount_vnd") != entitled
            or action.get("payer", "LOGIX") != "LOGIX"
            or action.get("basis") != "policy"
        ):
            ctx.log("guard_fix_refund", asked=action.get("amount_vnd"), entitled=entitled,
                    asked_payer=action.get("payer"))
            return Verdict.modify(
                "chuẩn hoá hoàn tiền theo tracking DB và chính sách hiệu lực",
                amount_vnd=entitled,
                payer="LOGIX",
                basis="policy",
            )
        return Verdict.allow()

    if tool == "file_carrier_fault":
        if order is None or pol is None:
            return Verdict.deny("thiếu đơn hàng hoặc chính sách hiệu lực để ghi lỗi hãng")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(pol, parcel, db_delay):
            ctx.log("guard_deny_fault", order_id=order["order_id"], db_delay=db_delay,
                    cause=parcel.get("delay_cause"))
            return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB và chính sách")
        if (
            action.get("parcel_id") != parcel["parcel_id"]
            or action.get("carrier_id") != parcel["carrier_id"]
            or action.get("delay_days") != db_delay
        ):
            return Verdict.modify(
                "chuẩn hoá kiện, hãng và độ trễ theo tracking DB",
                parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"],
                driver_id=parcel.get("driver_id"),
                delay_days=db_delay,
            )
        return Verdict.allow()

    if tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        allowed_fields = set(pol["carrier_notice_fields"]) if pol and pol.get("carrier_notice_fields") else None
        clean_payload = {k: v for k, v in payload.items() if allowed_fields is None or k in allowed_fields}
        if order is not None and "delay_days" in clean_payload:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            clean_payload["delay_days"] = H.db_delay_days(parcel, ctx.as_of)
        if clean_payload != payload:
            ctx.log("guard_sanitize_carrier_payload", dropped=sorted(set(payload) - set(clean_payload)))
            return Verdict.modify("lọc payload gửi hãng theo whitelist chính sách và tracking DB", payload=clean_payload)
        return Verdict.allow()

    return Verdict.allow()
