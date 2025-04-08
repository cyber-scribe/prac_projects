import requests;
import numpy as np;
# import pandas as pd;
import joblib;
import tensorflow as tf;
# from tensorflow.keras.models import load_model;
from flask import Flask, request, jsonify;



def get_real_time_weather(city):
    API_KEY = "YOUR_OPENWEATHER_API_KEY"  # Replace with your actual API key
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        weather_data = response.json()

        # Extract relevant weather features
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        precipitation = weather_data.get('rain', {}).get('1h', 0)  # Rainfall in last 1 hour
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']

        return np.array([[temperature, humidity, precipitation, wind_speed, pressure]])

    except Exception as e:
        print("Error fetching weather data:", e)
        return None
    


# Load Random Forest model for drought prediction
rf_model = joblib.load("random_forest_drought.pkl")

# Load LSTM model for heatwave prediction
lstm_model = load_model("lstm_heatwave.h5")
