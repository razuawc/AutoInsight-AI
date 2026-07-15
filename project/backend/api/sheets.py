from fastapi import APIRouter, Depends, HTTPException
from services.sheets_service import SheetsService
from database.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models.sheets import SheetsSyncLog

router = APIRouter()
sheets_service = SheetsService()


@router.post("/append")
async def append_to_sheet(row: list[str], db: AsyncSession = Depends(get_db)):
    success = await sheets_service.append_row(row)
    log = SheetsSyncLog(
        rows_appended=len(row) if success else 0,
        sync_status="success" if success else "failed",
    )
    db.add(log)
    await db.commit()
    return {"success": success}


@router.post("/append-summary")
async def append_summary(date: str, source: str, summary: str, insights: str, status: str):
    success = await sheets_service.append_summary_row(date, source, summary, insights, status)
    return {"success": success}


@router.get("/data")
async def get_sheet_data():
    data = await sheets_service.get_sheet_data()
    return {"data": data}
