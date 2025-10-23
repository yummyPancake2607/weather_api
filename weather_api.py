import os, requests

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def get_weather_from_api(city:str):
    url = f"{BASE_URL}/{city}?key={API_KEY}&unitGroup=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "city": data["resolvedAddress"],
        "temp": data["currentConditions"]["temp"],
        "conditions": data["currentConditions"]["conditions"]
    }
