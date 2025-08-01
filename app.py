import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# Train the model (you can later load from a file if already saved)
X = np.array([[151], [174], [138], [186], [128], [136], [179], [163],[152], [131]])  # Example heights
y = np.array([68, 81, 56, 91, 47, 57, 76, 72, 62, 48])  # Corresponding weights
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("Height to Weight Predictor")

# Input from user
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, step=1.0)

if st.button("Predict Weight"):
    input_height = np.array([[height]])
    predicted_weight = model.predict(input_height)
    st.success(f"Predicted Weight: {predicted_weight[0]:.2f} kg")
