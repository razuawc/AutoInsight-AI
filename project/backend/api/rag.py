from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from database.session import get_db
from models.execution import AIOutput
from services.rag_service import RAGService
from app.config import settings

router = APIRouter()
rag_service = RAGService()


@router.post("/query")
async def rag_query(question: str, db: AsyncSession = Depends(get_db)):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")

    result = await db.execute(
        select(AIOutput).order_by(desc(AIOutput.generated_at)).limit(10)
    )
    chunks = [row.output_content for row in result.scalars().all() if row.output_content]

    if not chunks:
        return {"answer": "No context available.", "chunks_used": 0}

    response = await rag_service.query(question, chunks)
    return response


@router.post("/embed")
async def create_embedding(text: str):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=400, detail="OpenAI API key not configured")
    embedding = await rag_service.create_embedding(text)
    return {"embedding": embedding[:10], "dimensions": len(embedding)}
