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
| **Random Forest Regressor** | 30325.896877 | 174.143323 | 78.592300 | 0.972352 |
| **HistGradientBoosting** | 30402.070451 | 174.361895 | 71.613211 | 0.972283 |

> **Analisis Hasil :**
> *Kedua algoritma menunjukkan performa prediktif yang sangat andal dengan nilai R-squared (R²) mencapai **0.972** (mampu menjelaskan 97.2% varians data kelistrikan).*
> *Terdapat *trade-off* yang menarik: **Random Forest** sedikit lebih unggul dalam meminimalisir kesalahan besar / outlier (ditunjukkan oleh nilai RMSE yang lebih rendah). Di sisi lain, **HistGradientBoosting** memiliki nilai MAE (Mean Absolute Error) yang lebih rendah (71.61 berbanding 78.59), yang berarti prediksi algoritma ini secara rata-rata lebih dekat dengan nilai aslinya. Mempertimbangkan efisiensi CPU dan waktu komputasi yang jauh lebih cepat, **HistGradientBoosting** tetap menjadi kandidat utama untuk di-deploy ke lingkungan produksi.*
---

## Setup & Instalasi Lokal

Sangat disarankan menggunakan *environment manager* seperti **Miniconda atau Anaconda** untuk menjaga isolasi dependensi paket Python Anda.

### Langkah 1: Kloning Repositori
Buka terminal atau Command Prompt Anda, lalu jalankan perintah kloning ini:
```bash
git clone [https://github.com/Ozen75/Daily-Energy-Estimator-for-Data-Center_ML-Project.git](https://github.com/Ozen75/Daily-Energy-Estimator-for-Data-Center_ML-Project.git)
cd Daily-Energy-Estimator-for-Data-Center_ML-Project
pip install -r requirements.txt
