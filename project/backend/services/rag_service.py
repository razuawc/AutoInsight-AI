from openai import AsyncOpenAI
from app.config import settings
import json


class RAGService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.embedding_model = "text-embedding-3-small"

    async def create_embedding(self, text: str) -> list[float]:
        response = await self.client.embeddings.create(
            model=self.embedding_model,
            input=text,
        )
        return response.data[0].embedding

    async def query(self, question: str, context_chunks: list[str]) -> dict:
        context = "\n\n".join(context_chunks)
        response = await self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a RAG assistant. Answer based on the provided context.",
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {question}",
                },
            ],
        )
        return {
            "answer": response.choices[0].message.content,
            "chunks_used": len(context_chunks),
        }
