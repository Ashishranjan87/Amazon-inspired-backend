from fastapi import APIRouter
from sqlalchemy import text

from core.redis import redis_client
from db.session import AsyncSessionLocal


router = APIRouter()


@router.get("/")
async def health_check():
    checks = {
        "api": "ok",
        "database": "ok",
        "redis": "ok",
    }

    try:
        async with AsyncSessionLocal() as db:
            await db.execute(text("SELECT 1"))
    except Exception:
        checks["database"] = "error"

    try:
        await redis_client.ping()
    except Exception:
        checks["redis"] = "error"

    status = "ok" if all(value == "ok" for value in checks.values()) else "degraded"

    return {
        "status": status,
        "checks": checks,
    }
