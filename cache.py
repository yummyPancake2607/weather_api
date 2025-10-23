import redis,os,json
from dotenv import load_dotenv

load_dotenv()


redis_url = os.getenv("REDIS_URL")
r = redis.Redis.from_url(redis_url)

def get_cache(city: str):
    cached = r.get(city)
    return json.loads(cached) if cached else None

def set_cache(city:str,data:dict,expiration:int = 43200):
    r.setex(city, expiration,json.dumps(data))
