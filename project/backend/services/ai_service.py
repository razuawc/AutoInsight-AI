from openai import AsyncOpenAI
from app.config import settings
from typing import Optional
import json


class AIService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    async def generate_summary(self, content: str, max_tokens: Optional[int] = None) -> dict:
        return await self._call_ai(
            system_prompt="You are a data analyst. Summarize the following data concisively, highlighting key points.",
            user_content=content,
            max_tokens=max_tokens or 500,
        )

    async def extract_insights(self, content: str) -> dict:
        return await self._call_ai(
            system_prompt="You are a business intelligence analyst. Extract key insights, patterns, and trends from the data.",
            user_content=content,
            max_tokens=1000,
        )

    async def classify_data(self, content: str, categories: list[str]) -> dict:
        categories_str = ", ".join(categories)
        return await self._call_ai(
            system_prompt=f"Classify the following content into one or more of these categories: {categories_str}. Return JSON.",
            user_content=content,
            max_tokens=500,
            response_format={"type": "json_object"},
        )

    async def generate_recommendations(self, content: str) -> dict:
        return await self._call_ai(
            system_prompt="You are a strategic advisor. Generate actionable recommendations based on the data.",
            user_content=content,
            max_tokens=1000,
        )

    async def generate_business_report(self, data_summary: str, data_sources: list[str]) -> dict:
        sources = ", ".join(data_sources)
        return await self._call_ai(
            system_prompt=f"Generate a comprehensive business report using data from: {sources}. Include executive summary, key findings, and recommendations.",
            user_content=data_summary,
            max_tokens=2000,
        )

    async def detect_trends(self, content: str) -> dict:
        return await self._call_ai(
            system_prompt="You are a trend analyst. Identify emerging trends, patterns, and anomalies in the data.",
            user_content=content,
            max_tokens=800,
        )

    async def _call_ai(
        self, system_prompt: str, user_content: str, max_tokens: int = 500, response_format: Optional[dict] = None
    ) -> dict:
        kwargs = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            "max_tokens": max_tokens,
            "temperature": settings.OPENAI_TEMPERATURE,
        }
        if response_format:
            kwargs["response_format"] = response_format

        response = await self.client.chat.completions.create(**kwargs)

        return {
            "content": response.choices[0].message.content,
            "model": response.model,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            },
        }
