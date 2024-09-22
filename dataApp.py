import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# Sidebar Configuration
st.sidebar.title("Patient Health Dashboard")
st.sidebar.subheader("Control Panel")

# Upload patient data (CSV or JSON)
uploaded_file = st.sidebar.file_uploader("Upload Patient Data (CSV/JSON)", type=["csv", "json"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)

    # Show the uploaded data
    st.subheader("Uploaded Patient Data")
    st.dataframe(df)

# Input patient details (Simulating new input)
st.header("Patient Information Form")
with st.form("patient_form"):
    name = st.text_input("Enter Patient's Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    weight = st.slider("Weight (kg)", 30, 150, 70)
    height = st.slider("Height (cm)", 100, 220, 170)
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"Patient {name} added successfully!")
    st.metric("BMI", round(weight / (height / 100) ** 2, 2))

# Displaying metrics summary
st.header("Summary Metrics")
st.metric("Blood Pressure", "120/80", delta="-2")
st.metric("Heart Rate", "72 bpm", delta="1 bpm")
st.metric("Temperature", "37°C")

# Charts Section - Simulating Patient Health Data
st.subheader("Health Data Visualization")

if uploaded_file:
    st.write("Blood Pressure Over Time")
    st.line_chart(df[['Date', 'Blood Pressure']].set_index('Date'))

    st.write("Heart Rate Over Time")
    st.line_chart(df[['Date', 'Heart Rate']].set_index('Date'))

    st.write("Weight Trend")
    st.area_chart(df[['Date', 'Weight']].set_index('Date'))

# Interactive Inputs
st.subheader("Simulate Health Changes")
blood_pressure = st.slider("Adjust Blood Pressure", 80, 180, 120)
heart_rate = st.slider("Adjust Heart Rate", 50, 150, 72)

if st.button("Update Health Data"):
    st.info(f"Simulated Blood Pressure: {blood_pressure}/80")
    st.info(f"Simulated Heart Rate: {heart_rate} bpm")

# Progress bar for file processing simulation
st.subheader("Data Processing Progress")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# Warning and error alerts
if blood_pressure > 140:
    st.warning("High blood pressure detected!")
if heart_rate < 60 or heart_rate > 100:
    st.error("Abnormal heart rate!")

# Visualization using Matplotlib
st.subheader("Matplotlib Chart Example")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Data")
ax.set_title("Sample Matplotlib Chart")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
st.pyplot(fig)

# Map to show hospital locations (if patient data contains locations)
st.subheader("Nearby Hospital Locations")
# Dummy coordinates data for a city map (e.g., latitude and longitude of hospitals)
map_data = pd.DataFrame({
    'lat': [37.7749, 37.7849, 37.7649],
    'lon': [-122.4194, -122.4094, -122.4294]
})
st.map(map_data)

# Color Picker for choosing patient theme (for demo purposes)
st.subheader("Customize UI Theme")
color = st.color_picker("Pick a theme color", "#00f900")
st.write(f"Selected theme color: {color}")

# Exception handling example
try:
    # Simulate a situation where a file is missing
    raise ValueError("Sample error: Patient data file not found")
except ValueError as e:
    st.exception(e)

# Balloons celebration for successful completion
st.balloons()

# Footer with some fine print or additional information
st.caption("This dashboard is for demo purposes only.")
