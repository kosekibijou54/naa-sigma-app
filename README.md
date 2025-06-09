# pgaa-sigma-app
# PGAA Sigma Prediction App

## 📌 Deskripsi
Aplikasi ini memprediksi nilai **Sigma (σ)** dari nilai **K₀** menggunakan model AI berbasis Gradient Boosting. Prediksi ini berguna dalam konteks **Prompt Gamma Activation Analysis (PGAA)** untuk membantu memperkirakan seberapa reaktif suatu isotop tanpa eksperimen laboratorium langsung.

---

## 🚀 Fitur Utama
- Input nilai K₀ secara manual
- Prediksi nilai cross-section (σ)
- Menampilkan 3 isotop dengan nilai σ paling mendekati hasil prediksi
- Menyediakan informasi unsur (nama dan simbol)


---

## 📁 Struktur Proyek
```
pgaa-sigma-app/
├── app.py                # Aplikasi utama Streamlit
├── train.py              # Skrip training model AI
├── model_sigma.pkl       # Model hasil training
├── pgaa_clean.csv         # Dataset utama
└── requirements.txt      # Daftar dependensi Python
```

---

## ⚙️ Cara Menjalankan Lokal
1. **Clone repository ini**
2. Install dependensi:
```
pip install -r requirements.txt
```
3. Jalankan training model (opsional jika model sudah tersedia):
```
python train.py
```
4. Jalankan aplikasi Streamlit:
```
streamlit run app.py
```

---

## ☁️ Deploy ke Streamlit Cloud
1. Upload seluruh isi folder ini ke GitHub
2. Buka [streamlit.io/cloud](https://streamlit.io/cloud) dan login
3. Klik **Deploy an app**, pilih repo dan `app.py` sebagai main file
4. Tunggu build selesai → Aplikasi Anda akan online

---


## 👨‍🔬 Dikembangkan oleh
Kelompok 1 Kecerdasan Buatan | 2025
