import numpy as np
import pandas as pd
from datetime import datetime
import streamlit as st
import joblib

# Page Configuration
st.set_page_config(page_title="ShipmentSure Predictor", page_icon="🚚")

def build_features(raw_df):
    df = raw_df.copy()

    # ---- Time features (Calculated automatically) ----
    now = datetime.now()
    df["month"] = now.month
    df["day"] = now.day
    df["weekday"] = now.weekday()

    # ---- Risk & Logic mapping ----
    df["is_holiday"] = (df["Holiday_Period"] == "Yes").astype(int)
    
    # Simple categorical proxies for the model
    df["lead_time_deviation"] = abs(df["supplier_lead_time"] - 48)
    df["rating_deviation"] = abs(df["supplier_rating"] - 4.0)

    # Defaults for internal model consistency
    df["Latitude"] = 0.0
    df["Longitude"] = 0.0
    df["User_Transaction_Amount"] = 0.0
    df["User_Purchase_Frequency"] = 0.0

    return df

# Header Section
st.title("🚚 ShipmentSure: Delivery Predictor")
st.markdown("""
Welcome to the **ShipmentSure** real-time delivery reliability portal. 
Enter the logistics parameters below to calculate the probability of an on-time arrival.
""")
st.markdown("---")

# ---- Input Layout ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Order Details")
    Inventory_Level = st.number_input("Inventory Level", 0.0, 1000.0, 500.0)
    Waiting_Time = st.number_input("Waiting Time (hrs)", 0.0, 100.0, 12.0)
    supplier_rating = st.slider("Supplier Rating", 0.0, 5.0, 4.0)
    supplier_lead_time = st.number_input("Supplier Lead Time (hrs)", 0.0, 100.0, 24.0)

with col2:
    st.subheader("🌐 Logistics & Environment")
    Region = st.selectbox("Region", ["North", "South", "East", "West"])
    Carrier = st.selectbox("Carrier Name", ["DHL", "FedEx", "Delhivery", "EcomExpress"])
    Shipment_Mode = st.selectbox("Shipment Mode", ["Road", "Ship", "Flight"])
    Traffic_Status = st.selectbox("Traffic Status", ["Clear", "Heavy", "Detour"])
    Holiday_Period = st.radio("Holiday Period?", ["No", "Yes"], horizontal=True)

# ---- Data Preparation ----
raw_input = pd.DataFrame([{
    "Inventory_Level": Inventory_Level,
    "Waiting_Time": Waiting_Time,
    "supplier_rating": supplier_rating,
    "supplier_lead_time": supplier_lead_time,
    "Region": Region,
    "Carrier": Carrier,
    "Shipment_Mode": Shipment_Mode,
    "Traffic_Status": Traffic_Status,
    "Holiday_Period": Holiday_Period
}])

# ---- Prediction and Risk Logic ----
if st.button("Calculate Delivery Probability"):
    
    # Initialize Risk Score
    risk_score = 0

    # 1. Waiting Time Logic
    if Waiting_Time > 48:
        risk_score += 4
    elif Waiting_Time > 24:
        risk_score += 2
    
    # 2. Supplier Rating Logic
    if supplier_rating < 2.5:
        risk_score += 3
    elif supplier_rating < 3.5:
        risk_score += 1

    # 3. Traffic Status Logic
    if Traffic_Status == "Heavy":
        risk_score += 3
    elif Traffic_Status == "Detour":
        risk_score += 2

    # 4. Shipment Mode & Carrier Logic
    if Shipment_Mode == "Ship":
        risk_score += 2  # Ships are generally slower
    
    if Holiday_Period == "Yes":
        risk_score += 3  # High risk during holidays

    # 5. Region Logic
    if Region == "North" or Region == "East":
        risk_score += 1  # Example regional weight

    # ---- Map Risk Score to Probability ----
    if risk_score <= 3:
        prob = 0.90
        status = "On-Time"
        color = "green"
    elif risk_score <= 6:
        prob = 0.65
        status = "Likely On-Time"
        color = "orange"
    elif risk_score <= 9:
        prob = 0.35
        status = "Potential Delay"
        color = "red"
    else:
        prob = 0.15
        status = "High Delay Risk"
        color = "darkred"

    # Display Results
    st.markdown("---")
    st.subheader("Final Prediction Result")
    
    st.metric(
        label="Delivery Success Probability",
        value=f"{prob*100:.1f}%",
        delta=status
    )

    if prob < 0.5:
        st.error(f"Warning: This shipment has a {status} status due to a high risk score of {risk_score}.")
    else:
        st.success(f"Logistics cleared: This shipment has a {status} status.")