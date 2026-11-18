# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): WeAreGuy
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-WeAreGuy-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Thanh Liêm | 2A202603358 | Kỹ sư cổng (Guards & Code) | x |
|   2 | Chử Văn Hiệp | 2A202603382 | Kỹ sư cổng (Eval, Trace & Monitors) | |
|   3 | Nguyễn Quang Vũ | 2A202603357 | Sản phẩm và kinh doanh | |
|   4 | Lê Văn Hoàng | 2A202603407 | Vận hành và pháp lý | |

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

## NguyenQuangVu-2A202603357

### Phần việc phụ trách

Sản phẩm và kinh doanh; `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`, Phiếu A (`A1` câu 1.1, `A4`–`A5`), Phiếu B (`B3`, `B7.4`, `B8` quyết định v1), Phiếu C (`C5` câu 3.2, `C10`, `C12` quyết định v2 & ba dòng bắt buộc).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## LeVanHoang-2A202603407

### Phần việc phụ trách

Vận hành và pháp lý; `config/operating_gates.json` mục `operations` & `legal`, `submission/submission.json`, Phiếu A (`A1` câu 1.2, `A2` câu 1.4), Phiếu B (`B4`–`B5`, `B7.5`–`B7.6` Runbook 1–3 & Giờ cao điểm), Phiếu C (`C3`, `C5` câu 3.3, `C11` Runbook 4–5).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
