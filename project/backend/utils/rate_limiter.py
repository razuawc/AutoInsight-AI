from fastapi import HTTPException, Request
from app.config import settings
import time
from collections import defaultdict

request_counts: dict = defaultdict(list)


async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    now = time.time()
    window = 60

    request_counts[client_ip] = [
        t for t in request_counts[client_ip] if now - t < window
    ]

    if len(request_counts[client_ip]) >= settings.RATE_LIMIT_PER_MINUTE:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

    request_counts[client_ip].append(now)
    response = await call_next(request)
    return response
