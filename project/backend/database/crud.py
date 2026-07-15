from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, text
from typing import Optional, List, TypeVar, Generic
from .base_repo import BaseRepository

T = TypeVar("T")

class CRUDBase(Generic[T]):
    def __init__(self, model: type[T]):
        self.model = model

    async def get(self, db: AsyncSession, id: str) -> Optional[T]:
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[T]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def create(self, db: AsyncSession, obj_in: dict) -> T:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, id: str, obj_in: dict) -> Optional[T]:
        db_obj = await self.get(db, id)
        if db_obj:
            for field, value in obj_in.items():
                setattr(db_obj, field, value)
            await db.commit()
            await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: str) -> bool:
        db_obj = await self.get(db, id)
        if db_obj:
            await db.delete(db_obj)
            await db.commit()
            return True
        return False

    async def count(self, db: AsyncSession) -> int:
        result = await db.execute(select(func.count()).select_from(self.model))
        return result.scalar()

    async def get_dashboard_stats(self, db: AsyncSession) -> dict:
        total = await self.count(db)

        success_result = await db.execute(
            select(func.count()).select_from(self.model).where(self.model.status == "completed")
        )
        success = success_result.scalar() or 0

        failed_result = await db.execute(
            select(func.count()).select_from(self.model).where(self.model.status == "failed")
        )
        failed = failed_result.scalar() or 0

        avg_time_result = await db.execute(
            select(func.avg(self.model.duration_ms)).where(self.model.status == "completed")
        )
        avg_time = avg_time_result.scalar() or 0

        return {
            "total_executions": total,
            "success_count": success,
            "failed_count": failed,
            "success_rate": round((success / total * 100), 2) if total > 0 else 0,
            "average_execution_time_ms": round(float(avg_time), 2),
        }
