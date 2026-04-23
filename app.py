import streamlit as st
import numpy as np
import pickle
import tensorflow as tf

model = tf.keras.models.load_model("model.keras")

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("log_columns.pkl", "rb") as f:
    log_cols = pickle.load(f)

with open("clip_values.pkl", "rb") as f:
    clip_vals = pickle.load(f)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check if it's Fraud or Not")

st.markdown("---")

st.subheader("Enter Input Values")

distance_from_home = st.number_input("Distance from Home", min_value=0.0)
distance_from_last_transaction = st.number_input("Distance from Last Transaction", min_value=0.0)
ratio_to_median_purchase_price = st.number_input("Ratio to Median Purchase Price", min_value=0.0)

repeat_retailer = st.selectbox("Repeat Retailer", [0, 1])
used_chip = st.selectbox("Used Chip", [0, 1])
used_pin_number = st.selectbox("Used PIN Number", [0, 1])
online_order = st.selectbox("Online Order", [0, 1])


if st.button("Predict"):

    input_data = np.array([[
        distance_from_home,
        distance_from_last_transaction,
        ratio_to_median_purchase_price,
        repeat_retailer,
        used_chip,
        used_pin_number,
        online_order
    ]])

    
    for i, col in enumerate(clip_vals.keys()):
        min_val, max_val = clip_vals[col]
        input_data[0][i] = np.clip(input_data[0][i], min_val, max_val)

    
    for col in log_cols:
        idx = list(clip_vals.keys()).index(col)
        input_data[0][idx] = np.log1p(input_data[0][idx])

    
    input_scaled = scaler.transform(input_data)

  
    prediction = model.predict(input_scaled)

    
    st.markdown("---")

    if prediction[0][0] > 0.5:
        st.error("🚨 Fraud Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")