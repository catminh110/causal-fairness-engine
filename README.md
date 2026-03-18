# 🚀 Causal Fairness Engine for Production ML

[cite_start]Dự án nghiên cứu về tối ưu hóa công bằng giao thoa nhân quả (Causal Intersectional Fairness) sử dụng thuật toán khám phá nhân quả tự động và can thiệp phản thực tế. [cite: 3, 4]

## 📌 Tính năng cốt lõi
* [cite_start]**Automated Causal Discovery:** Tự động phát hiện bias pathways bằng thuật toán PC và GES (Score-based) kết hợp Tiered Background Knowledge. [cite: 10, 15]
* [cite_start]**Intersectional Fairness:** Đạt DSC > 99% trên các nhóm giao thoa (Gender + Age + Race + Income) bằng PyTorch Multi-objective Optimization. [cite: 7, 11, 16]
* [cite_start]**Production Ready:** Hệ thống giám sát Real-time Dashboard và A/B Testing Framework tích hợp sẵn. [cite: 8, 16]

## 📂 Cấu trúc thư mục
* [cite_start]`data/`: Chứa các bộ dữ liệu thực tế (German Credit, Home Credit) và Synthetic data. [cite: 17, 21, 25]
* `notebooks/`: Quy trình thực nghiệm từ khám phá nhân quả đến đánh giá mô hình.
* [cite_start]`deployments/`: Mã nguồn giao diện giám sát Streamlit. [cite: 8]
* [cite_start]`docs/`: Báo cáo nghiên cứu chi tiết (`research_report.md`). [cite: 1-16]

## 🛠 Hướng dẫn cài đặt & Chạy dự án

1. **Cài đặt môi trường:**
   ```bash
   pip install pandas numpy networkx matplotlib causallearn scikit-learn torch streamlit
   ```

2. **Chạy khám phá nhân quả & huấn luyện:**
   Mở các file trong thư mục `notebooks/` theo thứ tự từ `01` đến `05`.

3. **Khởi động Dashboard giám sát:**
   ```bash
   streamlit run deployments/app.py
   ```

## 📊 Kết quả đạt được
* [cite_start]**Precision phát hiện thiên kiến:** > 95%. [cite: 6, 15]
* [cite_start]**Intersectional DSC:** 0.9994 (Mục tiêu > 0.90). [cite: 7, 16]
* [cite_start]**Accuracy Trade-off:** < 0.2% (Mục tiêu < 2%). [cite: 16]
* [cite_start]**Remediation Latency:** < 5 phút. [cite: 8, 16]

---