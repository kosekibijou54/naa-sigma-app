import streamlit as st
import pandas as pd
import numpy as np
import joblib
from mendeleev import element

# === Load model dan dataset ===
model = joblib.load("model_sigma.pkl")
df_model = pd.read_csv("naa_clean.csv")

# === Fungsi bantu: mapping Z ke simbol dan nama unsur ===
def get_element_info(z):
    try:
        e = element(z)
        return e.symbol, e.name
    except:
        return f"Z={int(z)}", "Unknown"

# === Judul Aplikasi ===
st.set_page_config(page_title="Prediksi Sigma dari K0", layout="centered")
st.title("\U0001F52C Prediksi Sigma Berdasarkan K₀")
st.markdown("Masukkan nilai K₀ untuk memprediksi nilai cross-section (\u03c3) dan menemukan isotop paling mendekati.")

# === Input User ===
k0_value = st.number_input("Masukkan nilai K₀:", min_value=1e-20, max_value=1.0, value=1e-11, format="%.2e")

# === Tombol prediksi ===
if st.button("\U0001F52E Prediksi Sigma"):
    input_df = pd.DataFrame({"K0": [k0_value]})
    pred_sigma = model.predict(input_df)[0]

    # Cari isotop terdekat
    df_model["Delta Sigma"] = np.abs(df_model["Sigma"] - pred_sigma)
    nearest = df_model.sort_values("Delta Sigma").head(3).copy()
    nearest[["Element", "Name"]] = nearest["Z"].apply(lambda z: pd.Series(get_element_info(z)))
    nearest["Half life (seconds)"] = nearest["Half life (seconds)"].apply(lambda x: f"{x:.2e}")

    # Tampilkan hasil
    st.success(f"Prediksi Sigma: {pred_sigma:.2e}")

    st.markdown("### Isotop Terdekat:")
    st.dataframe(
        nearest[["Isotope Name", "Element", "Name", "A", "Z", "E(y)", "Sigma", "Half life (seconds)", "Delta Sigma"]]
        .style.hide(axis="index")
    )
