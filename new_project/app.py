import requests;
import numpy as np;
import pandas as pd;
import joblib;
import tensorflow as tf;
from tensorflow.keras.models import load_model;
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


def predict_drought(city):
    real_time_data = get_real_time_weather(city)
    if real_time_data is not None:
        drought_risk = rf_model.predict(real_time_data)[0]
        return "⚠️ High Drought Risk" if drought_risk == 1 else "✅ No Drought Risk"
    return "Error in fetching weather data"

def predict_heatwave(city):
    real_time_data = get_real_time_weather(city)
    if real_time_data is not None:
        # Reshape input for LSTM
        lstm_input = real_time_data.reshape(1, real_time_data.shape[1], 1)
        temp_forecast = lstm_model.predict(lstm_input)[0][0]
        return f"🔥 Forecasted Temperature: {temp_forecast:.2f}°C (Possible Heatwave)" if temp_forecast > 40 else "✅ No Heatwave Risk"
    return "Error in fetching weather data"


app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    city = request.args.get('city', 'Los Angeles')
    drought_result = predict_drought(city)
    heatwave_result = predict_heatwave(city)

    return jsonify({
        "city": city,
        "drought_prediction": drought_result,
        "heatwave_prediction": heatwave_result
    })

if __name__ == '__main__':
    app.run(debug=True)