import streamlit as st
import pandas as pd
import joblib
import numpy as np
import time

# Konfigurasi Halaman Dashboard
st.set_page_config(
    page_title="Data Center Energy Predictor",
    page_icon="⚡",
    layout="centered"
)

# Fungsi untuk Memuat Model & Fitur
@st.cache_resource
def load_models_and_features():
    hgb = joblib.load('model_data_center_hgb.joblib')
    rf = joblib.load('model_data_center_rf.joblib')
    features = joblib.load('model_features.joblib')
    return hgb, rf, features

try:
    hgb_model, rf_model, model_features = load_models_and_features()
except FileNotFoundError:
    st.error("❌ File model (.joblib) atau fitur tidak ditemukan!")
    st.stop()

# Desain UI
st.title("⚡ Data Center Energy Consumption Predictor")
st.markdown("""
Aplikasi prediksi konsumsi listrik harian infrastruktur data center berdasarkan spesifikasi teknis dan metrik efisiensi operasional.  
*Projek Akhir Machine Learning - GDGoC*
""")
st.markdown("*oleh* Khalis Tofari")

st.divider()

# --- INPUT USER (FORM) ---
st.subheader("📋 Input Spesifikasi & Efisiensi Data Center")

# Baris 1: PUE, Capacity, dan WUE
col1, col2, col3 = st.columns(3)

with col1:
    capacity = st.number_input("Kapasitas Estimasi (MW)", min_value=0.1, max_value=1000.0, value=50.0, step=1.0)

with col2:
    pue = st.number_input("PUE (Power Usage Effectiveness)", min_value=1.0, max_value=3.0, value=1.5, step=0.01)

with col3:
    wue = st.number_input("WUE (L/kWh)", min_value=0.0, max_value=5.0, value=1.2, step=0.01,
                          help="Water Usage Effectiveness: Jumlah liter air yang digunakan per kilowatt-hour energi IT.")

# Baris 2: Tahun dan Kategori
col4, col5 = st.columns(2)

with col4:
    year = st.slider("Tahun Operasional", min_value=2015, max_value=2030, value=2026, step=1)
    facility_type = st.selectbox("Jenis Fasilitas", ["Hyperscale", "Colocation", "Enterprise/Standard"])

with col5:
    cooling_system = st.selectbox("Sistem Pendingin", ["Air Cooled", "Liquid Cooling", "Chilled Water", "Evaporative"])
    water_stress = st.selectbox("Kelangkaan Air Sekitar (Water Stress Tier)", ["Low", "Medium", "High"],
                                help="Tingkat kesulitan akses air bersih di lingkungan sekitar data center.")


# --- PILIHAN MODEL ---
st.divider()
st.subheader("🤖 Pengaturan Model Machine Learning")
pilihan_model = st.radio(
    "Pilih Algoritma untuk Prediksi:",
    ("HistGradientBoosting Regressor", "Random Forest Regressor"),
    horizontal=True
)

# --- PROSES PREDIKSI ---
if st.button("🚀 Hitung Estimasi Konsumsi Listrik", type="primary"):
    
    # TAMBAHAN BARU: Membungkus proses dalam st.spinner
    with st.spinner("⏳ Menganalisis parameter dan menjalankan model prediksi..."):
        
        # Simulasi proses komputasi agar UX terasa lebih natural
        time.sleep(1.5) 
        
        # 1. Masukkan input user ke dalam DataFrame
        data_input = pd.DataFrame([{
            'PUE': pue,
            'Estimated_Capacity_MW': capacity,
            'WUE_L_per_kWh': wue,
            'Year': year,
            'Facility_Type': facility_type,
            'Cooling_System_Type': cooling_system,
            'Surrounding_Water_Stress_Tier': water_stress
        }])
        
        # 2. Lakukan One-Hot Encoding pada input
        data_encoded = pd.get_dummies(data_input)
        
        # 3. Selaraskan matriks dengan fitur model saat training
        data_final = data_encoded.reindex(columns=model_features, fill_value=0)
        
        # 4. Eksekusi Prediksi
        if pilihan_model == "HistGradientBoosting Regressor":
            prediksi = hgb_model.predict(data_final)[0]
        else:
            prediksi = rf_model.predict(data_final)[0]
            
    # Kode di luar 'with st.spinner' akan dieksekusi setelah loading selesai
    # 5. Tampilkan Hasil
    st.success("🎉 Prediksi Berhasil!")
    
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(label="Estimasi Konsumsi Listrik", value=f"{prediksi:,.2f} MWh")
    with metric_col2:
        st.metric(label="Algoritma", value=pilihan_model.split()[0])
        
    st.info(f"💡 Interpretasi: Dengan kapasitas {capacity} MW, PUE {pue}, dan WUE {wue}, fasilitas ini diprediksi akan mengonsumsi **{prediksi:,.2f} Megawatt-hour (MWh)** listrik per harinya.")