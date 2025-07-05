# app.py
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load improved model
with open("ad_model.pkl", "rb") as f:
    model, features = pickle.load(f)

st.set_page_config(page_title="📈 Ad Budget → Sales Predictor", layout="centered")
st.title("📈 Advanced Ad Budget → Sales Predictor")

st.markdown("""
This app uses a **Polynomial + Ridge Regression** model to predict product sales based on ad spend.
""")

# Sidebar: Input sliders
st.sidebar.header("📥 Input Ad Budgets")
tv = st.sidebar.slider("TV", 0.0, 300.0, 100.0)
radio = st.sidebar.slider("Radio", 0.0, 50.0, 25.0)
newspaper = st.sidebar.slider("Newspaper", 0.0, 100.0, 30.0)

input_df = pd.DataFrame([[tv, radio, newspaper]], columns=features)

st.subheader("🔢 Input Values")
st.write(input_df)

# Predict
prediction = model.predict(input_df)[0]
st.subheader("🎯 Predicted Sales")
st.success(f"💰 {prediction:.2f} thousand units")

# Coefficients (show top 10 with actual feature names)
from sklearn.preprocessing import PolynomialFeatures

# Get polynomial feature names
poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit([[0, 0, 0]])  # Dummy fit to access feature names
feature_names = poly.get_feature_names_out(features)

# Match feature names with model coefficients
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": model.named_steps['model'].coef_
}).sort_values(by="Coefficient", ascending=False).head(10)

st.subheader("📊 Top Model Coefficients")
st.dataframe(coef_df)

# Plot
fig, ax = plt.subplots()
ax.barh(coef_df["Feature"], coef_df["Coefficient"], color="lightgreen")
ax.set_xlabel("Coefficient")
ax.set_title("Top Feature Impacts")
st.pyplot(fig)

st.dataframe(coef_df)

# Plot
fig, ax = plt.subplots()
ax.barh(coef_df["Feature"], coef_df["Coefficient"], color="lightgreen")
ax.set_xlabel("Coefficient")
ax.set_title("Top Feature Impacts")
st.pyplot(fig)

