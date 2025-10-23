# FastAPI Weather API (Redis Cache)

A FastAPI service that returns current weather for a given city using the Visual Crossing API, with Redis caching to reduce external calls. Interactive docs are available at /docs when running locally.

## Features
- GET /weather/{city} returns metric temperature and conditions.
- Redis cache stores responses to speed up repeated requests.
- Environment variables managed via .env.

## Project structure
```
.
├─ main.py            # FastAPI app and /weather/{city} route
├─ weather_api.py     # Visual Crossing API client (requests)
├─ cache.py           # Redis cache helpers, dotenv loading
├─ requirements.txt   # Dependencies
└─ .env               # WEATHER_API_KEY, REDIS_URL
```

## Requirements
Create requirements.txt with:
```
fastapi
uvicorn[standard]
requests
redis[hiredis]
python-dotenv
```

## Prerequisites
- Python 3.9+ installed.
- A Visual Crossing API key.
- A running Redis instance (e.g., redis://localhost:6379/0).

## Environment variables (.env)
Create a .env file in the project root:
```
WEATHER_API_KEY=your_visual_crossing_api_key_here
REDIS_URL=redis://localhost:6379/0
```

## Installation
```bash
# 1) Create and activate a virtual environment
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/LinuxMIT or your preferred license.
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

## Running
```bash
# Development (auto-reload)
uvicorn main:app --reload

# Or specify host/port
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open the interactive API docs:
```
http://127.0.0.1:8000/docs
```

## Usage example
Request:
```bash
curl http://127.0.0.1:8000/weather/London
```

Typical response:
```json
{
  "source": "api",
  "data": {
    "city": "London, England, United Kingdom",
    "temp": 14.2,
    "conditions": "Partially cloudy"
  }
}
```
Subsequent calls for the same city will return:
```json
{
  "source": "cache",
  "data": {
    "city": "London, England, United Kingdom",
    "temp": 14.2,
    "conditions": "Partially cloudy"
  }
}
```

## How it works
- main.py checks the Redis cache by city key; if found, returns cached data.
- If not cached, weather_api.py calls Visual Crossing, extracts currentConditions, then cache.py stores the result with an expiration.

## Configuration notes
- Cache TTL defaults to 12 hours (43200 seconds). Adjust in set_cache() if needed.
- The API uses metric units via unitGroup=metric in the request URL.
- Ensure .env is present and load_dotenv() is called before reading environment variables (already handled in cache.py).

## Troubleshooting
- 401/403 errors: verify WEATHER_API_KEY.
- Connection errors to Redis: confirm REDIS_URL and that Redis is running.
- CORS needs: add FastAPI CORSMiddleware if accessing from browsers across origins.

## Optional: Docker quickstart
```bash
# Start Redis
docker run -d --name weather-redis -p 6379:6379 redis:alpine

# Set REDIS_URL to: redis://localhost:6379/0
```

made by Lakshit Verma

project URL - https://roadmap.sh/projects/weather-api-wrapper-service
