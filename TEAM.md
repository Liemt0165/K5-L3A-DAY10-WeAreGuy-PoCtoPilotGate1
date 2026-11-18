# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): WeAreGuy
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-WeAreGuy-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S2

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Thanh Liêm | 2A202603358 | Kỹ sư cổng (Guards & Code) | x |
|   2 | Chử Văn Hiệp | 2A202603382 | Kỹ sư cổng (Eval, Trace & Monitors) | |
|   3 | Nguyễn Quang Vũ | 2A202603407 | Sản phẩm và kinh doanh | |
|   4 | Lê Văn Hoàng | 2A202603357 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công chi tiết (4 thành viên)

| STT | Vai | Trọng tâm phụ trách | File chính | Câu / Mục phiếu cầm bút |
| --: | --- | --- | --- | --- |
| 1 | Kỹ sư cổng (Guards & Code) | Quản lý repo Git, code cổng vòng 1 & 2, nhánh kỹ thuật HAZOP & Fault Tree | `lab10/guards.py` | B4 (nhánh kỹ thuật), B7.1 (câu 2.6), C4, C6, C7, C9 |
| 2 | Kỹ sư cổng (Eval, Trace & Monitors) | Chạy 7 lệnh đo (`eval`, `trace`, `gate`, `grade`, `checkpoint`, `check_submission`), đọc log `ticket@seed`, behavioral test (`--adhoc`), viết chỉ số theo dõi vòng 2 | `lab10/monitors.py`, nhật ký `B0`/`C0` | A2 (câu 1.3), B0, B1–B2 (câu 2.1–2.2), B7.2–B7.3 (câu 2.7–2.8), C0–C2 (câu 3.0–3.1), C8 (câu 3.6) |
| 3 | Sản phẩm và kinh doanh | Mục tiêu hệ thống, bản đồ dữ liệu & drift, viết & ký Bản tiêu chí, cổng `business`, Risk register, quyết định v1 & v2 | `config/acceptance_criteria.json`, `config/operating_gates.json` (`business`) | A1 (câu 1.1), A4–A5 (câu 1.6), B3 (câu 2.3), B7.4 (câu 2.9), B8 (v1), C5 (câu 3.2), C10, C12 (v2 & 3 dòng bắt buộc) |
| 4 | Vận hành và pháp lý | Mục tiêu vận hành, telemetry production, HAZOP mở rộng, Checklist 9 nhóm có PIC, cổng `operations` & `legal`, phần riêng theo thẻ, Runbook 1–5 & Giờ cao điểm, gom bài nộp | `config/operating_gates.json` (`operations`, `legal`), `submission/submission.json` | A1 (câu 1.2), A2 (câu 1.4), B4–B5 (câu 2.4), B7.5–B7.6 (câu 2.10), C3, C5 (câu 3.3), C11 |

> **Việc chung cả bàn:** Câu 1.5 (A3), Pre-mortem 4 lăng kính (B6, câu 2.5), đối chiếu pre-mortem & phân tích Fault Tree (C1, C6), thống nhất quyết định Gate 1 v1 (B8) và v2 (C12), Demo & phản biện (phút 200–230). Mỗi thành viên tự viết mục `## HoVaTen-MSSV` bên dưới trước khi nộp.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenThanhLiem-2A202603358

### Phần việc phụ trách

Trưởng nhóm · Kỹ sư cổng (Guards & Code); quản lý repo Git, `lab10/guards.py`, nhánh kỹ thuật ở Phiếu B (`B4`, `B7.1`) và Phiếu C (`C4`, `C6`, `C7`, `C9`).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## ChuVanHiep-2A202603382

### Phần việc phụ trách

Kỹ sư cổng (Eval, Trace & Monitors); chạy các lệnh đo và kiểm tra (`eval`, `trace`, `gate`, `grade`, `checkpoint`, `check_submission`), `lab10/monitors.py`, Phiếu A (`A2` câu 1.3), Phiếu B (`B0`, `B1`–`B2`, `B7.2`–`B7.3`), Phiếu C (`C0`–`C2`, `C8`).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LeVanHoang-2A202603357

### Phần việc phụ trách

Vai **Vận hành và pháp lý** (Thành viên 4):
- Phiếu A (`templates/form-a-criteria.md`): A1 (câu 1.2), A2 cột Telemetry production (câu 1.4).
- Phiếu B (`templates/form-b-evaluation-gates.md`): B4 bảng mở rộng ngoài kỹ thuật & B5 checklist 9 nhóm (câu 2.4), B7.5 Runbook 1–3 & B7.6 Giờ cao điểm (câu 2.10).
- Config cổng vận hành & pháp lý (`config/operating_gates.json` mục `operations`, `legal`).
- Khối 3 & bài nộp (thẻ `S2`): Phiếu C mục `C3.1`, `C5` (câu `3.3`), `C10`, `C11` và gom bài nộp `submission/submission.json`.

### Đóng góp cụ thể

- **Vòng 1:** Đã hoàn thiện mục tiêu nhìn từ chị Oanh (`NV-OANH`) và chị Hạnh (`NV-HANH`) ở câu 1.2 (Phiếu A mục A1), thiết kế telemetry production không cần nhãn cho tác động bên thứ ba (`file_carrier_fault`, `notify_carrier`) ở câu 1.4 (Phiếu A mục A2) với công thức tách riêng mẫu số cho từng tool; cấu hình cổng `operations` & `legal` trong `config/operating_gates.json`; hoàn thiện HAZOP mở rộng (Phiếu B mục B4), Checklist 9 nhóm có đủ PIC (B5), Runbook 1–3 (B7.5) và Giờ cao điểm (B7.6) khớp dữ liệu `data/world.json`.
- **Vòng 2 (thẻ `S2`):** Đối chiếu trace các ca `S2-01@11`, `S2-04@11`, `S2-20@11`, `S2-40..44@11` ở hai mốc `base` và `prepared`; hoàn thành phần riêng thẻ `S2` (**`C3.1` Mức kiểm soát của con người**: 5 dấu hiệu + bảng 5 dòng trả quyền duyệt và trừ `MERCHANT` về `NV-HANH`/`NV-OANH`), giả định môi trường sai ở **`C5` câu `3.3`**, dòng Risk register vận hành/pháp lý (**`C10`**, `merchant_debit_vnd`), và cập nhật Checklist + **Runbook 4–5 (`C11`)** (quy trình `NV-OANH` đối soát & hoàn trả shop `M-01` Gốm Bát Tràng Cô Lụa trước `16h`, kịch bản giờ cao điểm/LLM lỗi/mất lòng tin).
- Có sử dụng trợ lý AI để rà soát codebase (`lab10/agent.py`, `lab10/ops.py`, `lab10/tools.py`, `lab10/guards.py`), chạy trace kiểm chứng trên bộ `S2` và kiểm tính nhất quán giữa `config/operating_gates.json` với Runbook trong phiếu.

### Bằng chứng

- Commit vòng 1: `33283ff`, `16c9e29` (đã merge vào `main` tại `aef57db`), đồng bộ `1bb82de` (`R-S2-grade-20261118-164219-d3bfc7`).
- File đã điền phần của TV4: `TEAM.md`, `templates/form-a-criteria.md` (A1 câu 1.2, A2 câu 1.4), `config/operating_gates.json` (`operations`, `legal`), `templates/form-b-evaluation-gates.md` (B4 mở rộng, B5, B7.5, B7.6), `templates/form-c-incident.md` (`C3.1`, `C5` câu `3.3`, `C10`, `C11` Runbook 4–5), `submission/submission.json` (`team`, `members`).
- *(Còn chờ cả bàn hoàn tất `guards.py`/`monitors.py`, chạy lại `after`, chốt `C12` để cập nhật mã lần chạy cuối cùng, chép `decision_v2`/`three_lines` vào `submission/submission.json` và chạy `python3 -m lab10.check_submission --collect`.)*

### Exit ticket

- **Một điều học được:** Cổng cấu hình con số (`operating_gates.json`), quy trình đối soát/runbook (Runbook 4–5) và kiểm soát quyền con người (`C3.1`) quan trọng ngang cổng code — vì ngay cả khi code sửa số tiền, tổ chức vẫn phải biết giao ai khóa thao tác sai, đối soát với bên thứ ba (`M-01`, `NV-OANH`) trong bao lâu và giữ lòng tin người duyệt (`decision_note`, kiểm mẫu `10%`).
- **Một điều còn chưa chắc:** Trên production thật (không còn `MockLLM` tất định), biến thể văn bản cài lệnh mới trong `ticket.text` hoặc `checkout_note` có thể lách từ khóa nhận diện, nên trước Gate 2 cần đo thực tế tỉ lệ phát hiện `directive` và tần suất khiếu nại từ các shop đối tác.

## NguyenQuangVu-2A202603407

### Phần việc phụ trách

- Vai trong bàn: Sản phẩm và kinh doanh
- Trọng tâm phụ trách: Khối 1 (Phần A: phút 15–65): Xác định mục tiêu cấp hệ thống, xây dựng và ký Bản tiêu chí chấp nhận, thiết lập ranh giới đầu ra, xác định nhóm chỉ số kinh doanh & vận hành, soát 4 câu hỏi nghiệp vụ và niêm phong tiêu chí trước khi đo.
- File chính:
  - `config/acceptance_criteria.json`
  - `templates/form-a-criteria.md` (Phiếu A)
- Câu / Mục phiếu cầm bút:
  - Phiếu A: Mục A1 (câu 1.1), Mục A4–A5 (câu 1.6: xây dựng bộ tiêu chí, ranh giới đầu ra, 4 câu hỏi soát và ký tiêu chí).

### Đóng góp cụ thể

1. **Xác định mục tiêu cấp hệ thống (Phiếu A Mục A1 Câu 1.1)**:
   - Đặt mục tiêu giảm thời gian xử lý khiếu nại hoàn tiền từ 48 giờ xuống dưới 15 phút, giải phóng ít nhất 60% tải thủ công cho CSKH, duy trì chi phí trung bình dưới 8.000đ/ticket (thấp hơn làm tay 10.000đ) mà không làm phát sinh sai lệch tiền hoàn hoặc ghi lỗi oan cho đối tác vận chuyển.
2. **Xây dựng Bản tiêu chí chấp nhận (`config/acceptance_criteria.json` & Phiếu A Mục A4 Câu 1.6)**:
   - Xác định 5 ngưỡng an toàn bắt buộc: `pass_rate_min: 0.90`, `pass_k_min: 0.85`, `wrongful_refund_vnd_max: 0`, `wrongful_carrier_faults_max: 0`, `pii_leaks_max: 0`.
   - Đặt nhóm chỉ số hiệu quả kinh doanh & vận hành (`business_ops`): `cost_per_ticket_vnd_max: 8000`, `roi_min: 0.15`, `queue_stuck_max: 0`.
   - Thiết lập điều kiện dừng rõ ràng và quy tắc quyết định (`decision_rule`) cho cả 4 nhánh: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng.
3. **Thiết lập ranh giới đầu ra & soát 4 câu hỏi nghiệp vụ (Phiếu A Mục A4)**:
   - Đưa ra 2 ranh giới đầu ra: không tự động hoàn quá 200.000đ/ticket hoặc 300.000đ/ngày/khách mà không có chữ ký duyệt của trưởng ca CSKH; và ngưỡng chuyển người duyệt khi có sai lệch ngày trễ hoặc thuộc kho sỉ B2B.
   - Soát kỹ lưỡng 4 câu hỏi (lợi ích các bên, ai thiệt, ngày 1 vs ngày 1.000).
4. **Ký và niêm phong tiêu chí trước khi đo (Phiếu A Mục A5)**:
   - Chạy lệnh `python3 -m lab10.criteria sign` tạo file `config/acceptance_criteria.lock` với hash `359ec334c73bb10e6c9f584501b2f330a0f6bdcbf268eba586ce9ba6ce67e78a`, bảo đảm nguyên tắc "đặt luật trước, xem số sau".

### Bằng chứng

- Mã commit ký tiêu chí: `5fcda2e` (`Sign acceptance criteria` trên nhánh `nguyenquangvu-2A202603407`).
- File cấu hình đã ký: [config/acceptance_criteria.json](file:///d:/ProjectVin/K5-L3A-DAY10-WeAreGuy-PoCtoPilotGate1/config/acceptance_criteria.json)
- Mã hash niêm phong tiêu chí: `359ec334c73bb10e6c9f584501b2f330a0f6bdcbf268eba586ce9ba6ce67e78a` trong `config/acceptance_criteria.lock`.
- Phiếu A đã hoàn thành: [templates/form-a-criteria.md](file:///d:/ProjectVin/K5-L3A-DAY10-WeAreGuy-PoCtoPilotGate1/templates/form-a-criteria.md) (mục A1, A4, A5).

### Exit ticket

- **Một điều học được**: Bản tiêu chí chấp nhận (acceptance criteria) phải được toàn bộ nhóm thống nhất, gắn với hành động cụ thể nếu trượt ("nếu... thì...") và phải được ký niêm phong TRƯỚC khi chạy bất kỳ đánh giá nào để tránh thiên lệch xác nhận (confirmation bias).
- **Một điều còn chưa chắc**: Liệu ngưỡng escalation_rate ≤ 0.25 (25%) đã thực sự tối ưu trong giờ cao điểm khi lượng đơn trễ dồn về gấp ba hay có thể gây áp lực quá tải cục bộ cho trưởng ca duyệt hoàn tiền.
