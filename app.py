import streamlit as st
import pickle
import numpy as np 

# Load trained model
with open("model.pkl","rb") as file:
    model = pickle.load(file)

st.title("🚕 Uber Price Prediction App")
st.write("Enter all your trip details correctly to get predicted fare")

# 7 input features
pickup_longitude = st.number_input("pickup longitude")
pickup_latitude = st.number_input("pickup latitude")
dropoff_longitude = st.number_input("dropoff longitude")
dropoff_latitude = st.number_input("dropoff latitude")
passenger_count = st.number_input("passenger count", min_value=1, max_value=4, step=1)
pickup_hour = st.number_input("pickup hour (0-23)", min_value=0, max_value=23)

pickup_day = st.selectbox(
    "pickup day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

pickup_day_encoded = day_map[pickup_day]

# Predict
if st.button("Predict fare"):
    input_features = np.array([[
        pickup_longitude,
        pickup_latitude,
        dropoff_longitude,
        dropoff_latitude,
        passenger_count,
        pickup_hour,
        pickup_day_encoded
    ]])

    prediction = model.predict(input_features)
    st.success(f"Estimated fare: ${prediction[0]}")
