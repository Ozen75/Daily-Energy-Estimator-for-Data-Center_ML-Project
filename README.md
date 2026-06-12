# ⚡ Daily Energy Estimator for Data Center

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![GDGoC](https://img.shields.io/badge/GDGoC-Final%20Project-green.svg)

Repositori ini memuat projek akhir *Machine Learning* untuk **Google Developer Groups on Campus (GDGoC) Cohort 2026**. Proyek ini menghadirkan solusi analitik *end-to-end* untuk memprediksi konsumsi energi listrik harian (`Daily_Electricity_Usage_MWh`) pada infrastruktur data center global menggunakan pendekatan *Green Computing* yang efisien.

---

> **Catatan Teoretis (Design vs Operational PUE):** > Perusahaan biasanya menetapkan *Design PUE* di atas kertas melalui simulasi termal 3D CFD (*Computational Fluid Dynamics*). Namun, *Operational PUE* baru diketahui setelah data center berjalan satu tahun penuh. Model ini menjembatani celah tersebut dengan mengevaluasi performa operasional berdasarkan data historis global.

---
## Evaluasi Performa Model (Evaluation Metrics)

Tabel di bawah ini menunjukkan perbandingan metrik evaluasi numerik antara algoritma **Random Forest** dan **HistGradientBoosting** dalam memprediksi konsumsi energi listrik harian.

| Model | Mean Squared Error (MSE) | Root Mean Squared Error (RMSE) | Mean Absolute Error (MAE) | R-squared (R²) |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | 65249.2023 | 255.4392 | 87.6749 | 0.9996 |
| **HistGradientBoosting** | 65163.7915 | 255.2720 | 88.0833 | 0.9996 |

> **Analisis Hasil :**
> *Perbandingan evaluasi kinerja model. Kedua algoritma menunjukkan akurasi prediktif yang sangat luar biasa dengan nilai R-squared (R²) mencapai **0.9996** (mampu menjelaskan 99.96% varians data). **HistGradientBoosting** sedikit lebih unggul dalam meminimalisir kesalahan kuadrat (nilai MSE dan RMSE yang lebih rendah), menjadikannya kandidat algoritma paling optimal untuk tahap deployment (produksi), mengingat waktu komputasinya yang juga jauh lebih efisien.*
---

## Setup & Instalasi Lokal

Sangat disarankan menggunakan *environment manager* seperti **Miniconda atau Anaconda** untuk menjaga isolasi dependensi paket Python Anda.

### Langkah 1: Kloning Repositori
Buka terminal atau Command Prompt Anda, lalu jalankan perintah kloning ini:
```bash
git clone [https://github.com/Ozen75/Daily-Energy-Estimator-for-Data-Center_ML-Project.git](https://github.com/Ozen75/Daily-Energy-Estimator-for-Data-Center_ML-Project.git)
cd Daily-Energy-Estimator-for-Data-Center_ML-Project
pip install -r requirements.txt
