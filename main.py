from fastapi import FastAPI, HTTPException
from cache import get_cache, set_cache
from weather_api import get_weather_from_api

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city:str):
    cached_data = get_cache(city)
    if cached_data:
        return{"source": "cache", "data":cached_data}
    
    try:
        weather_data= get_weather_from_api(city)
    except HTTPException as e:
        raise e
    
    set_cache(city, weather_data)

    return{"source": "api", "data": weather_data}

