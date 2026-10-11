import numpy as np
import pandas as pd


def build_input_data(hour: int, workingday_val: int, temp: float, humidity: float, windspeed: float, weathersit_val: int) -> pd.DataFrame:
    return pd.DataFrame([
        {
            "hr": hour,
            "workingday": workingday_val,
            "temp_c": temp,
            "humidity": humidity,
            "windspeed_kmh": windspeed,
            "weathersit": weathersit_val,
        }
    ])


def predict_demand(model, input_data: pd.DataFrame) -> int:
    prediction = int(np.round(model.predict(input_data)[0]))
    return prediction
