from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from database.session import get_db
from models.execution import WorkflowExecution, AIOutput

router = APIRouter()


@router.get("/stats")
async def get_dashboard_stats(db: AsyncSession = Depends(get_db)):
    total = await db.execute(select(func.count(WorkflowExecution.id)))
    total_count = total.scalar() or 0

    success = await db.execute(
        select(func.count(WorkflowExecution.id)).where(WorkflowExecution.status == "completed")
    )
    success_count = success.scalar() or 0

    failed = await db.execute(
        select(func.count(WorkflowExecution.id)).where(WorkflowExecution.status == "failed")
    )
    failed_count = failed.scalar() or 0

    avg_time = await db.execute(
        select(func.avg(WorkflowExecution.duration_ms)).where(WorkflowExecution.status == "completed")
    )
    avg_execution_time = round(float(avg_time.scalar() or 0), 2)

    latest_ai = await db.execute(
        select(AIOutput).order_by(desc(AIOutput.generated_at)).limit(5)
    )
    latest_summaries = []
    for row in latest_ai.scalars().all():
        latest_summaries.append({
            "id": str(row.id),
            "prompt_type": row.prompt_type,
            "output_preview": row.output_content[:200] if row.output_content else "",
            "generated_at": row.generated_at.isoformat() if row.generated_at else None,
        })

    return {
        "total_executions": total_count,
        "success_count": success_count,
        "failed_count": failed_count,
        "success_rate": round((success_count / total_count * 100), 2) if total_count > 0 else 0,
        "average_execution_time_ms": avg_execution_time,
        "latest_ai_summaries": latest_summaries,
    }


@router.get("/execution-timeline")
async def get_execution_timeline(limit: int = 50, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(WorkflowExecution).order_by(desc(WorkflowExecution.created_at)).limit(limit)
    )
    executions = []
    for row in result.scalars().all():
        executions.append({
            "id": str(row.id),
            "workflow_name": row.workflow_name,
            "status": row.status,
            "duration_ms": row.duration_ms,
            "trigger_type": row.trigger_type,
            "started_at": row.started_at.isoformat() if row.started_at else None,
            "completed_at": row.completed_at.isoformat() if row.completed_at else None,
        })
    return executions
