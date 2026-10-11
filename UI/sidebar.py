import streamlit as st

from __init__ import DAY_LABELS, DEFAULT_HOUR, DEFAULT_HUMIDITY, DEFAULT_TEMP, DEFAULT_WEATHER_VALUE, DEFAULT_WINDSPEED, WEATHER_OPTIONS


def get_time_input() -> int:
    return st.sidebar.slider("Time of day (hr)", 0, 23, DEFAULT_HOUR)


def get_workingday_input() -> int|None:
    return st.sidebar.radio(
        "Day type",
        options=list(DAY_LABELS.keys()),
        format_func=lambda value: f"{DAY_LABELS[value]} ({value})",
    )


def get_temperature_input() -> float:
    return st.sidebar.slider("Feels-like temperature (°C)", -5.0, 40.0, DEFAULT_TEMP, step=0.5)


def get_humidity_input() -> float:
    return st.sidebar.slider("Relative humidity (%)", 10.0, 100.0, DEFAULT_HUMIDITY, step=1.0)


def get_wind_input() -> float:
    return st.sidebar.slider("Wind speed (km/h)", 0.0, 60.0, DEFAULT_WINDSPEED, step=1.0)


def get_weather_input() -> int|None:
    return st.sidebar.selectbox(
        "Weather conditions",
        options=list(WEATHER_OPTIONS.keys()),
        format_func=lambda value: WEATHER_OPTIONS[value],
        index=list(WEATHER_OPTIONS.keys()).index(DEFAULT_WEATHER_VALUE),
    )


def get_sidebar_inputs() -> dict:
    st.sidebar.header("Operational Settings")

    return {
        "hour": get_time_input(),
        "workingday_val": get_workingday_input(),
        "temp": get_temperature_input(),
        "humidity": get_humidity_input(),
        "windspeed": get_wind_input(),
        "weathersit_val": get_weather_input(),
    }
