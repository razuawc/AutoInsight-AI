from fastapi import APIRouter, Depends, HTTPException
from services.ai_service import AIService
from app.config import settings

router = APIRouter()
ai_service = AIService()


@router.post("/summarize")
async def summarize(content: str):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.generate_summary(content)
    return result


@router.post("/insights")
async def insights(content: str):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.extract_insights(content)
    return result


@router.post("/classify")
async def classify(content: str, categories: list[str]):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.classify_data(content, categories)
    return result


@router.post("/recommendations")
async def recommendations(content: str):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.generate_recommendations(content)
    return result


@router.post("/report")
async def business_report(data_summary: str, data_sources: list[str]):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.generate_business_report(data_summary, data_sources)
    return result


@router.post("/trends")
async def trends(content: str):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    result = await ai_service.detect_trends(content)
    return result
