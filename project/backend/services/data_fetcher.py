import httpx
from typing import Optional, Any
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


class DataFetcher:
    def __init__(self):
        self.timeout = httpx.Timeout(30.0)
        self.limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=30),
        retry=retry_if_exception_type((httpx.RequestError, httpx.HTTPStatusError)),
    )
    async def fetch(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout, limits=self.limits) as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            return {"status_code": response.status_code, "data": response.json(), "url": url}

    async def fetch_news(self, api_key: str, query: str = "technology", page_size: int = 10) -> dict:
        return await self.fetch(
            "https://newsapi.org/v2/everything",
            params={"q": query, "pageSize": page_size, "language": "en"},
            headers={"X-Api-Key": api_key},
        )

    async def fetch_weather(self, api_key: str, city: str = "London") -> dict:
        return await self.fetch(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
        )

    async def fetch_exchange_rates(self, base: str = "USD") -> dict:
        return await self.fetch(f"https://api.exchangerate-api.com/v4/latest/{base}")

    async def fetch_github_trending(self, query: str = "stars:>1000", sort: str = "stars", order: str = "desc") -> dict:
        return await self.fetch(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": sort, "order": order},
            headers={"Accept": "application/vnd.github.v3+json"},
        )
