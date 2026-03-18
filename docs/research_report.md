# BÁO CÁO NGHIÊN CỨU DỰ ÁN (RESEARCH REPORT)

[cite_start]**Đề tài:** Causal Intersectional Fairness Optimization with Automated Bias Pathway Discovery for Production ML Systems [cite: 1, 2]
**Tác giả:** [Tên của bạn]
**Ngày báo cáo:** 19/03/2026

---

## 1. Tóm tắt (Abstract)
[cite_start]Dự án tập trung giải quyết vấn đề thiên kiến giao thoa (intersectional bias) trong các hệ thống phê duyệt tín dụng tự động[cite: 4, 13]. [cite_start]Chúng tôi phát triển một **Causal Fairness Engine** có khả năng tự động khám phá các đường dẫn thiên kiến nhân quả từ dữ liệu quan sát[cite: 6, 15]. [cite_start]Bằng cách kết hợp thuật toán khám phá nhân quả (PC, GES) với tối ưu hóa đa mục tiêu trên nền tảng PyTorch, hệ thống đã đạt được chỉ số công bằng giao thoa $DSC > 99\%$ trong khi vẫn duy trì độ chính xác mô hình ở mức ổn định ($<0.2\%$ sụt giảm)[cite: 7, 16].

## 2. Khoảng trống nghiên cứu (Research Gap)
[cite_start]Các phương pháp tiếp cận truyền thống thường gặp 3 hạn chế chính mà dự án này đã khắc phục[cite: 12, 13]:
* [cite_start]**Tính đơn nhất:** Chỉ xử lý một thuộc tính bảo vệ (Single Attribute) thay vì các nhóm giao thoa (Intersectional Groups)[cite: 13].
* [cite_start]**Tính tĩnh:** Yêu cầu chuyên gia gán nhãn đồ thị nhân quả thủ công, không thể mở rộng cho dữ liệu lớn[cite: 13].
* [cite_start]**Thiếu khả năng triển khai:** Không có quy trình từ phát hiện đến tự động khắc phục (Auto-remediation) theo thời gian thực[cite: 13].

## 3. Phương pháp luận (Methodology)

### 3.1. Khám phá nhân quả tự động (Automated Causal Discovery)
[cite_start]Chúng tôi áp dụng quy trình hai giai đoạn[cite: 15]:
* [cite_start]**Giai đoạn 1:** Sử dụng thuật toán **GES (Greedy Equivalence Search)** để học cấu trúc từ dữ liệu[cite: 15].
* [cite_start]**Giai đoạn 2:** Áp dụng **Background Knowledge (Tiering)** để cưỡng chế logic nhân quả (ví dụ: Tuổi tác/Giới tính phải là biến gốc, không thể là kết quả của biến khác)[cite: 15].



### 3.2. Tối ưu hóa Công bằng (Fairness Optimization)
[cite_start]Hệ thống sử dụng **Multi-objective Loss Function** triển khai trên PyTorch[cite: 16]:
$$Loss = Loss_{BCE} + \lambda \cdot Loss_{Fairness}$$
[cite_start]Trong đó, $Loss_{Fairness}$ được tính dựa trên phương sai (variance) của tỷ lệ phê duyệt giữa các nhóm giao thoa trên các Tensor dữ liệu[cite: 16].

## 4. Kết quả thực nghiệm (Experimental Results)

### 4.1. Hiệu suất mô hình (Performance Metrics)
[cite_start]Dựa trên thực nghiệm với 10,000 mẫu dữ liệu sản xuất (Production Traffic)[cite: 16, 25]:

| Chỉ số | Mô hình Gốc (Biased) | Mô hình Nhân quả (Fair) | Tác động (Impact) |
| :--- | :--- | :--- | :--- |
| **Accuracy** | [cite_start]0.9007 [cite: 16] | [cite_start]0.9023 [cite: 16] | $+0.16\%$ (Cải thiện nhẹ) |
| **Intersectional DSC** | [cite_start]0.9825 [cite: 16] | [cite_start]0.9994 [cite: 16] | $+0.0169$ (Đạt mục tiêu $>0.90$) |

### 4.2. Kiểm định A/B Testing
[cite_start]Kết quả kiểm định T-test cho thấy giá trị $p-value = 0.7876$ ($>0.05$)[cite: 16]. [cite_start]Điều này khẳng định sự thay đổi về độ chính xác là không có ý nghĩa thống kê, chứng minh mô hình công bằng có thể thay thế mô hình cũ mà không gây rủi ro vận hành[cite: 16].

## 5. Hệ thống triển khai (Production Deployment)
* [cite_start]**Dashboard:** Giám sát thời gian thực các chỉ số DSC theo từng nhóm giao thoa (Gender + Race + Age)[cite: 8, 16].
* [cite_start]**Remediation:** Cơ chế tự động can thiệp nhân quả (Causal do-intervention) giúp sửa lỗi thiên kiến với độ trễ (latency) dưới 5 phút[cite: 8, 16].

## 6. Kết luận
Dự án đã thực hiện thành công một hệ thống **Production-ready Causal Fairness**. [cite_start]Kết quả cho thấy việc sử dụng tri thức nhân quả không chỉ giúp mô hình công bằng hơn một cách bền vững mà còn giúp nhà quản lý hiểu rõ "tại sao" thiên kiến xảy ra thông qua các đồ thị nhân quả trực quan[cite: 4, 25].

---

**Phụ lục đi kèm (Technical Appendix):**
* `notebooks/01_to_05`: Toàn bộ quy trình từ xử lý dữ liệu đến A/B Testing.
* `deployments/app.py`: Mã nguồn Dashboard giám sát.
* [cite_start]`data/`: Các tập dữ liệu German Credit, Home Credit và Synthetic [cite: 17-25].

---

