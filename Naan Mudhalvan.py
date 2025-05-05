import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Emission factors (kg CO2 per unit)
emission_factors = {
    'car_km': 0.2,
    'bus_km': 0.1,
    'bike_km': 0,
    'veg_meal': 1.0,
    'meat_meal': 2.5,
    'electricity_kwh': 0.5
}

def calculate_emissions(distance, mode, meal, electricity):
    total = 0
    total += emission_factors[f'{mode}_km'] * distance
    total += emission_factors[f'{meal}_meal']
    total += emission_factors['electricity_kwh'] * electricity
    return round(total, 2)

def get_recommendation(mode, meal):
    tips = []
    if mode == 'car':
        tips.append("Try using public transport or biking.")
    if meal == 'meat':
        tips.append("Consider reducing meat consumption.")
    tips.append("Use energy-efficient appliances to lower electricity usage.")
    return tips

st.title("EcoTrack: Carbon Footprint Tracker")

st.header("Enter Your Daily Activities")
distance = st.slider("Distance traveled (km):", 0, 100, 10)
mode = st.selectbox("Mode of transport:", ['car', 'bus', 'bike'])
meal = st.selectbox("Main meal type:", ['meat', 'veg'])
electricity = st.slider("Electricity used (kWh):", 0, 50, 5)

if st.button("Calculate Footprint"):
    footprint = calculate_emissions(distance, mode, meal, electricity)
    st.success(f"Your estimated daily carbon footprint: {footprint} kg CO2")

    tips = get_recommendation(mode, meal)
    st.subheader("Suggestions to Reduce Your Footprint:")
    for tip in tips:
        st.write("-", tip)

    # Basic visualization
    labels = ['Transport', 'Meal', 'Electricity']
    values = [emission_factors[f'{mode}_km'] * distance,
              emission_factors[f'{meal}_meal'],
              emission_factors['electricity_kwh'] * electricity]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Carbon Emission Breakdown")
    st.pyplot(fig)