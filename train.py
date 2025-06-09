import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("pgaa_clean.csv")
df_model = df.dropna(subset=["K0", "Sigma", "Sigma Uncertainty"])

# Training data
X = df_model[["K0", "Sigma Uncertainty"]]
y = df_model["Sigma"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model_sigma.pkl")
print("[OK] Model berhasil disimpan sebagai 'model_sigma.pkl'")

