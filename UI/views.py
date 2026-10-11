import numpy as np
import pandas as pd
import streamlit as st

from __init__ import BASELINE_DEMAND, BASE_LAT, BASE_LON


def render_estimated_demand(prediction: int):
    st.subheader("Estimated Demand")
    st.metric(
        label="Bikes required / hour",
        value=f"{prediction} bikes",
        delta=f"{prediction - BASELINE_DEMAND} vs overall average",
    )


def render_logistics_diagnosis(prediction: int):
    st.subheader("Logistics Diagnosis")
    if prediction >= 400:
        st.error(
            "⚠️ **Critical peak demand**: High risk of empty stations. "
            "Deploy rebalancing vans to exchange hubs (train stations, universities)."
        )
    elif prediction >= 180:
        st.warning(
            "⚡ **High activity**: Steady flow. "
            "Monitor peripheral stations and prepare rotations."
        )
    else:
        st.success(
            "✅ **Smooth traffic / Quiet period**: Stable fleet. "
            "Ideal time for technical maintenance and battery charging."
        )


def render_station_map(input_data: pd.DataFrame):
    st.subheader("Simulated spatial pressure on the network")
    seed_value = int(input_data.iloc[0]["hr"]) + int(input_data.iloc[0]["workingday"])
    np.random.seed(seed_value)

    n_stations = 30
    simulated_stations = pd.DataFrame({
        "lat": BASE_LAT + np.random.normal(0, 0.02, size=n_stations),
        "lon": BASE_LON + np.random.normal(0, 0.03, size=n_stations),
    })
    st.map(simulated_stations)


def render_model_performance(metrics: dict):
    st.subheader("Model Performance")
    st.write(f"- **R^2 score** : `{metrics['r2']}`")
    st.write(f"- **Mean absolute error (MAE)** : `±{metrics['mae']} bikes`")
    st.write(f"- **Root mean square error (RMSE)** : `±{metrics['rmse']} bikes`")


def render_input_vector(input_data: pd.DataFrame):
    st.subheader("Input vector sent")
    st.dataframe(input_data, hide_index=True)


def render_demand_status(prediction: int):
    col_metric, col_status = st.columns([1, 2])

    with col_metric:
        render_estimated_demand(prediction)

    with col_status:
        render_logistics_diagnosis(prediction)


def render_model_metrics(metrics: dict, input_data: pd.DataFrame):
    st.divider()
    col_map, col_details = st.columns([2, 1])

    with col_map:
        render_station_map(input_data)

    with col_details:
        render_model_performance(metrics)
        render_input_vector(input_data)
