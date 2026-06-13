import json
from typing import Any
from core.redis import redis_client

async def get_cache(key:str):
    cached_data = await redis_client.get(key)
    if cached_data is None:
        return None

    return json.loads(cached_data)

async def set_cache(key:str, value:Any, expire_seconds: int):
    await redis_client.set(key, json.dumps(value),ex=expire_seconds)

async def delete_cache(key:str):
    await redis_client.delete(key)

async def delete_cache_pattern(pattern:str):
    keys = await redis_client.keys(pattern)
    if keys:
        await redis_client.delete(*keys)