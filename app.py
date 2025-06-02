import streamlit as st
import pandas as pd
import numpy as np
import joblib
import altair as alt

# === Load model dan dataset ===
model = joblib.load("model_sigma.pkl")
df_model = pd.read_csv("naa_clean.csv")

Z_TO_ELEMENT = {
    1: ("H", "Hydrogen"), 2: ("He", "Helium"), 3: ("Li", "Lithium"), 4: ("Be", "Beryllium"),
    5: ("B", "Boron"), 6: ("C", "Carbon"), 7: ("N", "Nitrogen"), 8: ("O", "Oxygen"),
    9: ("F", "Fluorine"), 10: ("Ne", "Neon"), 11: ("Na", "Sodium"), 12: ("Mg", "Magnesium"),
    13: ("Al", "Aluminium"), 14: ("Si", "Silicon"), 15: ("P", "Phosphorus"), 16: ("S", "Sulfur"),
    17: ("Cl", "Chlorine"), 18: ("Ar", "Argon"), 19: ("K", "Potassium"), 20: ("Ca", "Calcium"),
    21: ("Sc", "Scandium"), 22: ("Ti", "Titanium"), 23: ("V", "Vanadium"), 24: ("Cr", "Chromium"),
    25: ("Mn", "Manganese"), 26: ("Fe", "Iron"), 27: ("Co", "Cobalt"), 28: ("Ni", "Nickel"),
    29: ("Cu", "Copper"), 30: ("Zn", "Zinc"), 31: ("Ga", "Gallium"), 32: ("Ge", "Germanium"),
    33: ("As", "Arsenic"), 34: ("Se", "Selenium"), 35: ("Br", "Bromine"), 36: ("Kr", "Krypton"),
    37: ("Rb", "Rubidium"), 38: ("Sr", "Strontium"), 39: ("Y", "Yttrium"), 40: ("Zr", "Zirconium"),
    41: ("Nb", "Niobium"), 42: ("Mo", "Molybdenum"), 43: ("Tc", "Technetium"), 44: ("Ru", "Ruthenium"),
    45: ("Rh", "Rhodium"), 46: ("Pd", "Palladium"), 47: ("Ag", "Silver"), 48: ("Cd", "Cadmium"),
    49: ("In", "Indium"), 50: ("Sn", "Tin"), 51: ("Sb", "Antimony"), 52: ("Te", "Tellurium"),
    53: ("I", "Iodine"), 54: ("Xe", "Xenon"), 55: ("Cs", "Cesium"), 56: ("Ba", "Barium"),
    57: ("La", "Lanthanum"), 58: ("Ce", "Cerium"), 59: ("Pr", "Praseodymium"), 60: ("Nd", "Neodymium"),
    61: ("Pm", "Promethium"), 62: ("Sm", "Samarium"), 63: ("Eu", "Europium"), 64: ("Gd", "Gadolinium"),
    65: ("Tb", "Terbium"), 66: ("Dy", "Dysprosium"), 67: ("Ho", "Holmium"), 68: ("Er", "Erbium"),
    69: ("Tm", "Thulium"), 70: ("Yb", "Ytterbium"), 71: ("Lu", "Lutetium"), 72: ("Hf", "Hafnium"),
    73: ("Ta", "Tantalum"), 74: ("W", "Tungsten"), 75: ("Re", "Rhenium"), 76: ("Os", "Osmium"),
    77: ("Ir", "Iridium"), 78: ("Pt", "Platinum"), 79: ("Au", "Gold"), 80: ("Hg", "Mercury"),
    81: ("Tl", "Thallium"), 82: ("Pb", "Lead"), 83: ("Bi", "Bismuth"), 84: ("Po", "Polonium"),
    85: ("At", "Astatine"), 86: ("Rn", "Radon"), 87: ("Fr", "Francium"), 88: ("Ra", "Radium"),
    89: ("Ac", "Actinium"), 90: ("Th", "Thorium"), 91: ("Pa", "Protactinium"), 92: ("U", "Uranium"),
    93: ("Np", "Neptunium"), 94: ("Pu", "Plutonium"), 95: ("Am", "Americium"), 96: ("Cm", "Curium")
}

def get_element_info(z):
    return Z_TO_ELEMENT.get(int(z), (f"Z={int(z)}", "Unknown"))

# === Judul Aplikasi ===
st.set_page_config(page_title="Prediksi Sigma dari K0", layout="centered")
st.title("\U0001F52C Prediksi Sigma Berdasarkan K₀")
st.markdown("Masukkan nilai K₀ untuk memprediksi nilai cross-section (\u03c3) dan menemukan isotop paling mendekati.")

# === Input User ===
k0_value = st.number_input("Masukkan nilai K₀:", min_value=1e-20, max_value=1.0, value=1e-11, format="%.2e")

# === Tombol prediksi ===
if st.button("\U0001F52E Prediksi Sigma"):
    default_uncertainty = df_model["Sigma Uncertainty"].median()
    input_df = pd.DataFrame({
    "K0": [k0_value],
    "Sigma Uncertainty": [default_uncertainty]
})
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
