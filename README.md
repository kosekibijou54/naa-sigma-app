# naa-sigma-app
# NAA Sigma Prediction App

## 📌 Deskripsi
Aplikasi ini memprediksi nilai **Sigma (σ)** dari nilai **K₀** menggunakan model AI berbasis Gradient Boosting. Prediksi ini berguna dalam konteks **Neutron Activation Analysis (NAA)** untuk membantu memperkirakan seberapa reaktif suatu isotop tanpa eksperimen laboratorium langsung.

---

## 🚀 Fitur Utama
- Input nilai K₀ secara manual
- Prediksi nilai cross-section (σ)
- Menampilkan 3 isotop dengan nilai σ paling mendekati hasil prediksi
- Menyediakan informasi unsur (nama dan simbol)
- Kategori Half-life (Sangat Pendek, Pendek, Sedang, Panjang)

---

## 📁 Struktur Proyek
```
naa-sigma-app/
├── app.py                # Aplikasi utama Streamlit
├── train.py              # Skrip training model AI
├── model_sigma.pkl       # Model hasil training
├── naa_clean.csv         # Dataset utama
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

## 📚 Referensi
- De Corte, F. (1986). *The k₀-Standardization Method*
- IAEA TECDOC-1215: *Neutron Activation Analysis using k₀-method*
- scikit-learn, streamlit, pandas, periodictable

---

## 👨‍🔬 Dikembangkan oleh
Tim NAA-AI | 2025
