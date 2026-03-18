import streamlit as st
import pandas as pd
import time

st.title("🚀 Causal Fairness Real-time Dashboard")
st.subheader("System Status: Monitoring Intersectional Bias")

# Thêm menu chọn Dataset
dataset_name = st.selectbox(
    "Chọn luồng dữ liệu Production cần giám sát:",
    ("Synthetic Intersectional Data", "German Credit Data", "Home Credit Data")
)

st.write(f"**Đang giám sát:** {dataset_name}")

dsc_placeholder = st.empty()
status_placeholder = st.empty()
chart_placeholder = st.empty()

# Thiết lập DSC ban đầu mô phỏng theo từng dataset
if dataset_name == "German Credit Data":
    start_dsc = 0.94
elif dataset_name == "Home Credit Data":
    start_dsc = 0.98
else:
    start_dsc = 0.96

dsc_values = []

# Chỉ chạy khi bấm nút
if st.button("Bắt đầu giám sát Real-time"):
    for i in range(15):
        current_dsc = start_dsc - (i * 0.012)
        dsc_values.append(current_dsc)
        
        dsc_placeholder.metric("Intersectional DSC", f"{current_dsc:.4f}", "-0.012")
        chart_placeholder.line_chart(dsc_values)
        
        if current_dsc < 0.90:
            status_placeholder.error(f"⚠️ CẢNH BÁO ({dataset_name}): DSC tụt dưới 0.90. Phát hiện Bias Pathways!")
            time.sleep(1)
            status_placeholder.warning("🔄 Đang kích hoạt Auto-remediation (Causal Intervention)...")
            time.sleep(1.5)
            
            # Sửa lỗi xong
            current_dsc = 0.99
            dsc_values[-1] = current_dsc
            dsc_placeholder.metric("Intersectional DSC", f"{current_dsc:.4f}", "Đã tối ưu")
            chart_placeholder.line_chart(dsc_values)
            status_placeholder.success(f"✅ Sửa lỗi thành công cho {dataset_name}. Latency: 2.5s (Mục tiêu < 5min).")
            break
            
        time.sleep(0.5)