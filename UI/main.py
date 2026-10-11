import streamlit as st

from __init__ import MODEL_FILE
from sidebar import get_sidebar_inputs
from prediction import build_input_data, predict_demand
from model_loader import load_model
from views import render_demand_status, render_model_metrics
st.set_page_config(
    page_title="Smart City - Bike Sharing",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 Predictive Monitoring of Bike Sharing Demand")
st.markdown(
    "Decision-support application for urban fleet rebalancing based on "
    "environmental and time-based data."
)

inputs = get_sidebar_inputs()
input = build_input_data(
    hour=inputs["hour"],
    workingday_val=inputs["workingday_val"],
    temp=inputs["temp"],
    humidity=inputs["humidity"],
    windspeed=inputs["windspeed"],
    weathersit_val=inputs["weathersit_val"]
)
try:
    model, feature_names, metrics = load_model(MODEL_FILE)
    predictions = predict_demand(model, input)
    render_demand_status(predictions)
    render_model_metrics(metrics, input)
except FileNotFoundError as exc:
    st.error(f"Model loading error: {exc}")
    st.stop()