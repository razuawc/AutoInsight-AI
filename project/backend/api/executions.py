from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from database.session import get_db
from models.execution import WorkflowExecution, RawAPIResponse, CleanedData, AIOutput
from database.crud import CRUDBase
import uuid

router = APIRouter()
crud = CRUDBase(WorkflowExecution)


@router.get("/")
async def list_executions(skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(WorkflowExecution).order_by(desc(WorkflowExecution.created_at)).offset(skip).limit(limit)
    )
    executions = []
    for row in result.scalars().all():
        executions.append({
            "id": str(row.id),
            "workflow_name": row.workflow_name,
            "status": row.status,
            "trigger_type": row.trigger_type,
            "duration_ms": row.duration_ms,
            "error_message": row.error_message,
            "started_at": row.started_at.isoformat() if row.started_at else None,
            "completed_at": row.completed_at.isoformat() if row.completed_at else None,
            "created_at": row.created_at.isoformat() if row.created_at else None,
        })
    return executions


@router.get("/{execution_id}")
async def get_execution(execution_id: str, db: AsyncSession = Depends(get_db)):
    try:
        uid = uuid.UUID(execution_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid execution ID")

    result = await db.execute(select(WorkflowExecution).where(WorkflowExecution.id == uid))
    execution = result.scalar_one_or_none()
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")

    raw_result = await db.execute(
        select(RawAPIResponse).where(RawAPIResponse.execution_id == uid)
    )
    raw_data = []
    for row in raw_result.scalars().all():
        raw_data.append({
            "id": str(row.id),
            "source": row.source,
            "endpoint": row.endpoint,
            "status_code": row.status_code,
            "fetched_at": row.fetched_at.isoformat() if row.fetched_at else None,
        })

    ai_result = await db.execute(
        select(AIOutput).where(AIOutput.execution_id == uid)
    )
    ai_data = []
    for row in ai_result.scalars().all():
        ai_data.append({
            "id": str(row.id),
            "prompt_type": row.prompt_type,
            "output_content": row.output_content,
            "model": row.model,
            "generated_at": row.generated_at.isoformat() if row.generated_at else None,
        })

    return {
        "execution": {
            "id": str(execution.id),
            "workflow_name": execution.workflow_name,
            "status": execution.status,
            "trigger_type": execution.trigger_type,
            "duration_ms": execution.duration_ms,
            "error_message": execution.error_message,
            "started_at": execution.started_at.isoformat() if execution.started_at else None,
            "completed_at": execution.completed_at.isoformat() if execution.completed_at else None,
        },
        "raw_responses": raw_data,
        "ai_outputs": ai_data,
    }


@router.post("/")
async def create_execution(data: dict, db: AsyncSession = Depends(get_db)):
    execution = WorkflowExecution(
        workflow_name=data.get("workflow_name", "Manual Trigger"),
        status="running",
        trigger_type=data.get("trigger_type", "api"),
        started_at=func.now(),
    )
    db.add(execution)
    await db.commit()
    await db.refresh(execution)
    return {"id": str(execution.id), "status": "running"}
