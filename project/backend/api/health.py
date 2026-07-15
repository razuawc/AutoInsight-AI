from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database.session import get_db
from app.config import settings
import httpx
import time

router = APIRouter()


@router.get("/")
async def health_check():
    return {"status": "healthy", "service": settings.APP_NAME, "version": "1.0.0"}


@router.get("/database")
async def database_health(db: AsyncSession = Depends(get_db)):
    start = time.time()
    try:
        await db.execute(text("SELECT 1"))
        latency = int((time.time() - start) * 1000)
        return {"status": "healthy", "latency_ms": latency}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


@router.get("/redis")
async def redis_health():
    try:
        import redis.asyncio as redis
        r = redis.from_url(settings.REDIS_URL)
        start = time.time()
        await r.ping()
        latency = int((time.time() - start) * 1000)
        await r.aclose()
        return {"status": "healthy", "latency_ms": latency}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


@router.get("/n8n")
async def n8n_health():
    try:
        start = time.time()
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.N8N_WEBHOOK_URL}/healthz", timeout=5)
            latency = int((time.time() - start) * 1000)
            return {"status": "healthy" if response.status_code == 200 else "unhealthy", "latency_ms": latency}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


@router.get("/openai")
async def openai_health():
    if not settings.OPENAI_API_KEY:
        return {"status": "not_configured"}
    try:
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        await client.models.list()
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


@router.get("/all")
async def all_health(db: AsyncSession = Depends(get_db)):
    db_health = await database_health(db)
    redis_health_result = await redis_health()
    n8n_health_result = await n8n_health()
    openai_health_result = await openai_health()

    all_healthy = all(
        h.get("status") == "healthy"
        for h in [db_health, redis_health_result, n8n_health_result]
        if h.get("status") != "not_configured"
    )

    return {
        "overall": "healthy" if all_healthy else "degraded",
        "services": {
            "database": db_health,
            "redis": redis_health_result,
            "n8n": n8n_health_result,
            "openai": openai_health_result,
        },
    }
