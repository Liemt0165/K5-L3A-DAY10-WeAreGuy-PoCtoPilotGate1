# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** `WeAreGuy`

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | |
| Việc người dùng cần làm xong | |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | |
| Trường then chốt quyết định tiền và lỗi hãng | |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `__________`, `__________`, `__________` để giúp `__________` làm được `__________`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `__________`, `__________`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `__________`. Dấu hiệu nhìn thấy sớm nhất: `__________`.

**Ví dụ drift trong 3 tháng tới** (lấy từ dòng "thế giới thật làm dữ liệu lệch"): cái gì đổi `____` · đổi ngày nào `____` ·
trường nào cho thấy `____` · con số nào của Bản tiêu chí bị ảnh hưởng `____`.
Đây là đầu vào đổi hay quan hệ vào–ra đổi? Chỉ số nào sẽ phát hiện? `__________`

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `________________` (gợi ý: `issue_refund`, `file_carrier_fault`, `notify_carrier`)

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (viết bằng dữ kiện của lab) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| | WRONG | | | | |
| | INVALID | | | | |
| | INCOMPLETE | | | | |
| | PERTURBED | | | | |
| | INCAPABLE | | | | |

Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần | Guideword | Lệch cụ thể | Hậu quả, cho ai | Cổng đề xuất: code hay con số nào trong `config/operating_gates.json` |
|---|---|---|---|---|
| **Người duyệt** (vận hành) | INCAPABLE | Chỉ để 1 người trực (6 ca/giờ = 10 phút/ca) hoặc nhân viên không tin trợ lý nên kiểm lại 100% ca tự động, trong khi giờ cao điểm có > 10 ca tới dồn trong 1 giờ | Hàng chờ vượt SLA 60 phút, nhiều ca bị ùn sang cuối ca, khách chờ phản hồi lâu và trưởng ca `NV-HANH` quá tải | `operations.reviewers_on_shift: 2` (12 ca/giờ), `operations.max_queue_wait_minutes: 60`, bật `operations.decision_note: true` (giảm thời gian kiểm lại còn 0.4 ca), `operations.review_sampling_pct: 10`, `operations.approver_id: "NV-HANH"` |
| **Ngân sách** (kinh doanh) | WRONG | Trợ lý hoàn tự động nhiều ca liên tiếp hoặc tính sai số tiền vượt trần ngân sách ngày của Finance (`2.000.000đ/ngày`) hoặc vượt `300.000đ/khách/ngày` mà không chặn | LogiX thâm hụt ngân sách ngày, chi phí mỗi ticket vượt chi phí làm tay (`10.000đ`) khiến ROI âm; chị Oanh (`NV-OANH`) không khớp được sổ quỹ | `business.daily_refund_cap_vnd` (<= `2000000` theo `ops_limits`), `business.cost_budget_per_ticket_vnd` (<= `1500` trần LLM) trong `config/operating_gates.json` kết hợp kiểm soát trần theo khách trong `lab10/guards.py` |
| **Phạm vi pilot** (kinh doanh) | INVALID | Cho chạy tự động trên cả nhóm đơn giá trị lớn hoặc kho sỉ (`HCM-B2B`, đơn từ 2 triệu đồng) hay nhóm ca trợ lý thường phải chuyển người (tốn thêm 10.000đ công duyệt + tiền LLM) | Tỉ lệ chuyển người cao, chi phí mỗi ticket ở kho đó đắt hơn làm tay (> `10.000đ`), tổng tiết kiệm ròng bị âm | Đặt `business.pilot_scope` (`mode` theo kho/tỉ lệ phù hợp sau khi đọc khối `theo kho và hãng` của `lab10.eval`) và đặt `business.roi_min` để report cảnh báo sớm khi ROI dưới ngưỡng |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED / WRONG | Với đơn quà tặng (`is_gift: true`), payload gửi `notify_carrier` kèm `recipient_contact` (tên, SĐT người nhận) hoặc chép nguyên `customer_note` có PII khách tự gõ; hoặc `file_carrier_fault` tự gán lỗi `"CARRIER"` khi `delay_cause` trên tracking DB bị trống (`null`) | Lộ PII người nhận hàng (người không tham gia giao dịch ticket) ra bên thứ ba; hãng vận chuyển (`GHSH`, `VNX`, `MKD`, `DNB`) bị phạt tiền oan (`80.000–150.000đ/strike`) và có nguy cơ bị đình chỉ sai (`suspend_after_strikes_7d`) | `legal.pii_fields_blocked_to_third_party: ["recipient_contact", "customer_note", "recipient", "phone", "name", "street"]` và `legal.carrier_fault_requires_recorded_cause: true` trong `config/operating_gates.json` |

**Ví dụ mẫu (`issue_refund`, đừng chép):** tham số `amount_vnd` · WRONG · số tiền tính từ số ngày khách tự khai · LogiX mất
tiền, hãng bị kéo theo một lỗi · hiện chỉ có trần "không vượt tổng tiền đơn" · cổng ghi so với quyền lợi tính từ DB (chặn).

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi (Phiếu B mục B2) | `pass_rate`, `pass_k`, `T-002@55` đã xếp loại và vá cổng | Chưa *(cập nhật sau B1–B2, B7.1)* | *(cập nhật sau mã lần chạy `base` & `base · after`, mục B1–B2)* | Chử Văn Hiệp |
| 2 | Dữ liệu | Bản đồ dữ liệu (Phiếu B mục B3, câu 2.3): trường nào là nguồn sự thật, trường nào là bản sao | Nguồn sự thật (`orders`, `parcels`, `policies`), ví dụ drift | Chưa *(cập nhật sau B3)* | *(cập nhật mục B3)* | Nguyễn Quang Vũ |
| 3 | Bảo mật | Một vòng HAZOP với guideword PERTURBED (Phiếu B mục B4): chữ nào đi vào model mà không do LogiX viết | `ticket.text`, `order.checkout_note`, chống directive/override | Chưa *(cập nhật sau B4 tool & B7.1)* | Mục B4 mở rộng (`PERTURBED`), chờ B4 tool & `lab10/guards.py` | Nguyễn Thanh Liêm |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S2, S8 có thêm mục mức kiểm soát (Phiếu C mục C3) | Công tắc `on/off`, `write_gate`, `approver_id` hợp lệ | Chưa *(cập nhật sau B7.1)* | `config/switches.json`, `config/operating_gates.json` (`operations.approver_id: NV-HANH`), chờ `lab10/guards.py` | Nguyễn Thanh Liêm |
| 5 | Hiệu năng, hạ tầng | Đội tự ước tính; HAZOP guideword INCAPABLE: LLM không trả lời thì sao; số người duyệt và số ca mỗi giờ | Dự phòng LLM 429/fallback, SLA hàng chờ 60 phút, công suất duyệt | Chưa *(cập nhật sau B1 & B7.1)* | `config/operating_gates.json` (`reviewers_on_shift: 2`, `review_capacity_per_hour: 12`, `max_queue_wait_minutes: 60`), mục B4 & B7.6 | Lê Văn Hoàng |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report: chi phí mỗi ticket so với làm tay, ROI, tiền LLM ticket đắt nhất; `config/operating_gates.json` mục `business` | `cost_per_ticket_vnd` < 10.000đ, `ROI` dương, trần LLM ≤ 1.500đ | Chưa *(cập nhật sau B1 & B7.4)* | `config/operating_gates.json` (`business`), chờ mã lần chạy `base · after` | Nguyễn Quang Vũ |
| 7 | Vận hành | Runbook (Phiếu B mục B7.5–B7.6) + `config/operating_gates.json` mục `operations` (PIC, người duyệt, số người trực, điều kiện dừng, kênh báo tin) + metric trong `monitors.py` | Đủ `pic`, `approver_id`, `alert_channel`, `stop_conditions`, Runbook 1–3 khớp config | Chưa *(vòng 1 xong B7.5–B7.6 & `operating_gates.json`; còn `monitors.py` vòng 2)* | `config/operating_gates.json` (`operations`: `NV-TUNG`, `#ops-gate1-alerts`, `decision_note: true`, `review_sampling_pct: 10`), Phiếu B mục B7.5–B7.6 | Lê Văn Hoàng |
| 8 | Con người, pháp lý | Bên thứ ba (hãng, tài xế, shop, người nhận quà, người đứng tên duyệt); `config/operating_gates.json` mục `legal`; thẻ S6, S7, S8 có mục riêng ở Phiếu C mục C3 | Chặn PII gửi hãng, chỉ ghi lỗi hãng khi có `delay_cause` trong DB | Xong *(vòng 1; kiểm lại ở vòng 2 nếu trúng thẻ S6–S8)* | `config/operating_gates.json` (`legal`: `pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause: true`), Phiếu B mục B4 & B7.5 | Lê Văn Hoàng |
| 9 | Quyết định | Câu tiêu chí (Phiếu A mục A4) + hash Bản tiêu chí đã ký + quyết định Gate 1 (Phiếu B mục B8, Phiếu C mục C12) | Ký `acceptance_criteria.json` trước khi `eval`; chốt `v1`, `v2` | Chưa *(cập nhật sau A5 & B8)* | *(chờ commit `Sign acceptance criteria`, file `.lock`, mục B8)* | Nguyễn Quang Vũ |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register (Phiếu C mục C10).

---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được hôm nay? (trace / data / config nào) | Thành cổng phòng ngừa nào (code hay config) / hay vào risk register |
|---|---|---|---|
| | Kỹ thuật | | |
| | Kinh doanh | | |
| | Con người và vận hành | | |
| | Pháp lý | | |
| | | | |

---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | | |
| `business.cost_budget_per_ticket_vnd` | | |
| `business.pilot_scope` (all / warehouse / percent) | | |
| `business.roi_min` | | |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** Lê Văn Hoàng (`2A202603357`)

#### Runbook 1 · Ai chịu trách nhiệm

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | Lê Thanh Tùng (`NV-TUNG`) | Giám sát vận hành chung, theo dõi cảnh báo, điều phối trực ca và cập nhật cấu hình vận hành | `#ops-gate1-alerts` |
| Người duyệt đứng tên các khoản vượt hạn mức | Trần Thị Hạnh (`NV-HANH`) | Đứng tên duyệt các khoản hoàn vượt `auto_limit_vnd`, xử lý ca chuyển người (`escalated`) và rà soát kiểm mẫu 10% | `#ops-gate1-alerts` (ưu tiên gọi trực tiếp khi chạm ngưỡng ĐỎ) |
| Người giữ công tắc tắt từng thao tác ghi | Lê Thanh Tùng (`NV-TUNG`) | Chỉnh `config/switches.json` (`on` → `off`) và thu hẹp `business.pilot_scope` khi chạm điều kiện dừng | `#ops-gate1-alerts` |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | Phạm Kiều Oanh (`NV-OANH` — hãng & shop) · Trần Thị Hạnh (`NV-HANH` — khách & người nhận quà) | Tiếp nhận khiếu nại phạt oan / trừ sai shop / lộ PII, đối soát sổ cái & thông báo thu hồi/đính chính | `#ops-gate1-alerts` & kênh đối soát tuần với hãng/shop |

Số người trực duyệt mỗi ca: `2` · Mỗi giờ duyệt được: `12` ca *(lưu ý nếu tăng lên `3` người ở vòng 2 phải nâng `operations.review_capacity_per_hour` lên `18` hoặc `null` để không bị kìm công suất)* · Phạm vi pilot: `Toàn bộ` (`mode: "all", percent: 100` trong `config/operating_gates.json`; cập nhật lại nếu TV3 thu hẹp kho/tỉ lệ trong B7.4)

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | `hàng chờ người duyệt` → `lâu nhất ... phút` (`lab10.eval`) / `thời gian chờ lâu nhất (phút)` (`lab10.grade` · `ops.queue.wait_max_min`) | `≤ 35` phút | `> 35` đến `≤ 60` phút → Báo `#ops-gate1-alerts`, chuẩn bị gọi người duyệt thứ 3 | `> 60` phút (chạm `max_queue_wait_minutes: 60`) → Gọi thêm người và nâng `review_capacity_per_hour`, hoặc thu hẹp `pilot_scope` | `NV-TUNG` gọi người · `NV-HANH` duyệt |
| Số ca bị ùn | `hàng chờ người duyệt` → `... ca bị ùn` (`lab10.eval`) / `số ca bị ùn` (`lab10.grade` · `ops.queue.stuck`) | `0` ca | Hàng chờ dồn `> 8` ca chưa tới hạn → Tăng tốc kiểm mẫu bằng `decision_note` | `≥ 1` ca bị ùn → Thu hẹp `pilot_scope` hoặc chuyển bớt ticket sang làm tay | `NV-TUNG` |
| Chi phí mỗi ticket so với làm tay | `chi phí mỗi ticket` & `tiết kiệm ròng mỗi ngày · ROI` (`lab10.eval`) / `chi phí mỗi ticket (đ) · làm tay`, `ROI`, `số kho đắt hơn làm tay`, `theo kho và hãng` (`lab10.grade` · `ops.cost`) | `< 7.500đ/ticket` và `ROI ≥ 0.2` *(tham chiếu cấu hình vòng 1: `5.821đ`, `ROI 0.69`)* | `7.500đ–9.500đ/ticket` hoặc có kho `> làm tay` ở khối `theo kho và hãng` → Soát tỉ lệ chuyển người và tiền LLM | `≥ 10.000đ/ticket` (đắt hơn làm tay) hoặc `ROI < 0` → Tắt ở kho lỗ qua `pilot_scope` / dừng thu hẹp | `NV-TUNG` + Sản phẩm & Kinh doanh |
| Tổng hoàn tự động trong ngày so với trần | `tổng hoàn tự động một ngày` (`lab10.eval`) / `tổng hoàn tự động một ngày (đ) · ngân sách` (`lab10.grade` · `ops.refund.auto_refund_day_max_vnd`) | `≤ 70%` ngân sách ngày (`≤ 1.400.000đ`) | `> 70%` đến `≤ 90%` ngân sách/trần ngày → Cảnh báo `#ops-gate1-alerts`, kiểm tra bất thường | `> 90%` hoặc chạm trần `daily_refund_cap_vnd` → Cổng tự chặn hoàn tự động, chuyển toàn bộ sang `NV-HANH` duyệt | `NV-HANH` |
| Tiền hoàn sai | `wrongful_refund_vnd` & `tổng hoàn tự động một ngày` → `hoàn sai ngày tệ nhất` (`lab10.eval`) / `tiền hoàn sai ngày tệ nhất (đ) · ngân sách` (`lab10.grade`) | `0đ` | Không có mức vàng với tiền hoàn sai (bất kỳ sai lệch chính sách nào đều điều tra ngay) | `> 0đ` → Chặn/tắt `issue_refund` trong `config/switches.json`, kiểm tra trace & vá `guards.py` | `NV-TUNG` · `NV-OANH` đối soát |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân (pháp lý) | `wrongful_carrier_faults`, `pii_leaks` (`lab10.eval`) & `pháp lý: lỗi ghi oan cho hãng (bên thứ ba)` (`lab10.grade`) + khối `theo kho và hãng` | `0` lỗi hãng oan · `0` ca lộ PII | Một hãng bị ghi `> 2` lỗi tự động/ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`) → `NV-OANH` kiểm tra chéo tracking | `≥ 1` lỗi ghi oan cho hãng hoặc `≥ 1` ca lộ PII → Tắt ngay `file_carrier_fault` / `notify_carrier`, tra khối `theo kho và hãng` để gửi đính chính | `NV-TUNG` bấm tắt · `NV-OANH` xử lý hãng |
| (tín hiệu riêng của bàn) Mất lòng tin người duyệt (`recheck` 100%) | `tỉ lệ chuyển người duyệt` → `nhân viên kiểm lại ...% quyết định tự động` (`lab10.eval`) / `nhân viên kiểm lại quyết định tự động (%)` (`lab10.grade`) · `ops.queue.trust` trong `report.json` | `recheck_pct = 10%` (`trust: "đạt"` hoặc `"không áp dụng"`) | `review_sampling_pct < 10%` hoặc `decision_note: false` → Bật lại chuẩn trong `config/operating_gates.json` | `recheck_pct = 100%` hoặc `trust: "chưa đạt"` (dùng `approval` không hợp lệ / sai `approver_id`) → Tạm dừng tự động hoá để sửa nguồn phê duyệt | `NV-HANH` · `NV-TUNG` |

#### Runbook 3 · Điều kiện dừng và cách dừng

- Dừng một phần (tắt một thao tác ghi, thu hẹp phạm vi) khi: Có `≥ 1` ca ghi lỗi oan cho hãng (`file_carrier_fault` → `"off"`), hoặc `≥ 1` ca lộ PII (`notify_carrier` → `"off"`), hoặc một kho có chi phí mỗi ticket vượt `10.000đ`/ca bị ùn cục bộ (cắt kho đó khỏi `business.pilot_scope`).
- Dừng hẳn khi: Có `≥ 1` ca hoàn sai nặng / lặp lại chưa rõ nguyên nhân, hoặc tổng tiền hoàn tự động chạm ngưỡng nguy hiểm, hoặc hàng chờ bị ùn quá `60` phút trên toàn hệ thống mà không gọi kịp người trực, hoặc `ops.queue.trust` chuyển `"chưa đạt"` (`recheck_pct = 100%`) do dùng phê duyệt không hợp lệ.
- Cách dừng, từng bước (công tắc nào trong `config/switches.json`, dòng nào trong `config/operating_gates.json`):
  1. Phát thông báo khẩn trên kênh `#ops-gate1-alerts` kèm mã lần chạy / `ticket_id`.
  2. Dừng một phần: mở `config/switches.json`, chuyển thao tác vi phạm (`"file_carrier_fault"`, `"notify_carrier"`, hoặc `"issue_refund"`) từ `"on"` sang `"off"`. Hoặc mở `config/operating_gates.json` thu hẹp `business.pilot_scope` (`"mode": "warehouse"` chỉ giữ kho an toàn hoặc giảm `"percent"`).
  3. Dừng hẳn: chuyển `"issue_refund"`, `"file_carrier_fault"`, `"notify_carrier"` về `"off"` trong `config/switches.json` (hoặc tạm đưa toàn bộ ticket về xử lý tay).
- Từ tín hiệu đỏ đến lúc dừng xong tối đa `15` phút; người bấm: `NV-TUNG` (Lê Thanh Tùng)
- Khi đã dừng, ticket đang chờ đi đâu, ai xử lý: Tất cả ticket đang ở trạng thái chờ hoặc đến mới trong thời gian dừng được chuyển về quy trình xử lý tay tại CSKH dưới sự điều phối của `NV-HANH` (ưu tiên các ca đã chờ > 35 phút trước để đảm bảo SLA 60 phút); `NV-OANH` đối soát các bút toán đã phát sinh trước thời điểm dừng.
- Điều kiện để bật lại, ai ký: Đã xác định nguyên nhân gốc trên trace, sửa xong trong `lab10/guards.py` / `config/operating_gates.json`, chạy `python3 -m lab10.eval --suite base --stage after` (và `python3 -m lab10.grade --incident Sx` ở vòng 2) đạt `0` hoàn sai, `0` lỗi hãng oan, `0` lộ PII và `0` ca bị ùn; cả `NV-TUNG` (PIC vận hành) và `NV-HANH` (Trưởng ca CSKH) ký xác nhận trên `#ops-gate1-alerts` trước khi đổi công tắc về `"on"`.

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | Một ca dài `480` phút (8 giờ); ngày thường bộ nền có `22` ticket/ca (~`2,75` ticket/giờ). Giờ cao điểm (ngày sale, sau bão) lượng ticket dồn gấp 3 (~`66` ticket/ca, tương đương `8–15` ticket dồn vào 1 giờ; theo quy ước mô phỏng hàng chờ, nếu `10` ca cần duyệt tới dồn mỗi 2 phút trong 18 phút đầu giờ cao điểm thì `1` người trực bị ùn `2` ca chờ 64–72 phút > hạn `60` phút). |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | `2` người trực mỗi ca (khớp `operations.reviewers_on_shift: 2`), công suất `12` ca/giờ (`6 ca/giờ/người` theo `ops_facts.review_capacity_per_reviewer_per_hour`), do Trưởng ca Trần Thị Hạnh (`NV-HANH`) phụ trách duyệt chính và phối hợp thêm 1 nhân viên CSKH trực cùng ca; Lê Thanh Tùng (`NV-TUNG`) trực giám sát cảnh báo. |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | Khi hàng chờ tích luỹ `> 8` ca hoặc thời gian chờ lâu nhất vượt `35` phút (quá nửa SLA `60` phút) hoặc tỉ lệ chuyển người vượt `30%`, `NV-TUNG` gọi bổ sung người trực thứ 3 ngay trên `#ops-gate1-alerts` và nâng `reviewers_on_shift: 3`, `review_capacity_per_hour: 18` (hoặc `null`) để tránh bị kìm công suất. |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | Nếu đã gọi thêm người nhưng vẫn có `≥ 1` ca chờ chạm `60` phút (`queue.stuck > 0`) hoặc chạm trần tiền hoàn ngày / phát sinh lỗi pháp lý: `NV-TUNG` phối hợp `NV-HANH` thu hẹp `business.pilot_scope` (giảm `"percent"` hoặc chỉ giữ kho ổn định) hoặc chuyển công tắc trong `config/switches.json` sang `"off"` để chặn rủi ro lan rộng. |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | Theo `data/world.json` → `ops_facts.reviewer_standby_fee_vnd`, mỗi người trực thêm tốn `30.000đ/ca` phí giữ chỗ (`standby_cost_per_day_vnd` trong `report.json`). Trên 22 ticket/ngày ở bộ nền, tăng từ `1` (`4.203đ/ticket`, `ROI 1.34`) lên `2` người trực kèm `decision_note: true` và `review_sampling_pct: 10` làm chi phí tăng lên `5.821đ/ticket` (`standby` `60.000đ/ngày`, `ROI 0.69`), vẫn rẻ hơn làm tay (`10.000đ/ticket`) và ROI dương; nếu thêm quá nhiều người (3–4 người) khi lượng ticket ngày thường thấp, phí giữ chỗ `90.000–120.000đ/ngày` sẽ đẩy `cost_per_ticket_vnd` tiệm cận hoặc vượt `10.000đ` và kéo ROI về âm. |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt phần nào, vì sao | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
