import pandas as pd
import requests
from datetime import datetime

WEATHER_CSV_URL = "https://raw.githubusercontent.com/vega/vega-datasets/master/data/seattle-weather.csv"

def fetch_weather_air_quality():
    # Weather CSV
    weather_df = pd.read_csv(WEATHER_CSV_URL)
    weather_df["date"] = pd.to_datetime(weather_df["date"])

    # Air Quality API (Seattle)
    aq_url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality"
        "?latitude=47.6062"
        "&longitude=-122.3321"
        "&daily=pm2_5,pm10"
        "&timezone=auto"
    )
    aq_data = requests.get(aq_url).json()

    aq_df = pd.DataFrame({
        "date": pd.to_datetime(aq_data["daily"]["time"]),
        "pm2_5": aq_data["daily"]["pm2_5"],
        "pm10": aq_data["daily"]["pm10"]
    })

    merged = pd.merge(weather_df, aq_df, on="date", how="inner")

    merged.to_csv("data/weather_air_quality.csv", index=False)
    return merged
