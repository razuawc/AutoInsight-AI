from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
from models.execution import WorkflowExecution, RawAPIResponse, CleanedData, AIOutput
from services.notification_service import NotificationService
from datetime import datetime
import uuid

router = APIRouter()
notifier = NotificationService()


@router.post("/n8n/workflow-completed")
async def n8n_workflow_completed(payload: dict, db: AsyncSession = Depends(get_db)):
    execution_id = payload.get("execution_id")
    workflow_name = payload.get("workflow_name", "n8n Workflow")
    status = payload.get("status", "completed")
    error = payload.get("error")

    try:
        uid = uuid.UUID(execution_id) if execution_id else uuid.uuid4()
    except ValueError:
        uid = uuid.uuid4()

    execution = WorkflowExecution(
        id=uid,
        n8n_workflow_id=payload.get("workflow_id"),
        n8n_execution_id=payload.get("n8n_execution_id"),
        workflow_name=workflow_name,
        status=status,
        trigger_type=payload.get("trigger_type", "webhook"),
        started_at=datetime.utcnow(),
        completed_at=datetime.utcnow() if status in ("completed", "failed") else None,
        duration_ms=payload.get("duration_ms"),
        error_message=error,
    )
    db.add(execution)
    await db.commit()

    if status == "failed":
        await notifier.notify_workflow_error(workflow_name, error or "Unknown error")
    else:
        await notifier.notify_workflow_completed(workflow_name, status, payload.get("duration_ms", 0))

    return {"received": True, "execution_id": str(uid)}


@router.post("/n8n/data-fetched")
async def n8n_data_fetched(payload: dict, db: AsyncSession = Depends(get_db)):
    raw = RawAPIResponse(
        execution_id=uuid.UUID(payload["execution_id"]) if payload.get("execution_id") else None,
        source=payload.get("source", "unknown"),
        endpoint=payload.get("endpoint"),
        request_params=payload.get("params"),
        response_body=payload.get("data"),
        status_code=payload.get("status_code", 200),
    )
    db.add(raw)
    await db.commit()
    return {"received": True, "id": str(raw.id)}


@router.post("/n8n/ai-output")
async def n8n_ai_output(payload: dict, db: AsyncSession = Depends(get_db)):
    ai = AIOutput(
        execution_id=uuid.UUID(payload["execution_id"]) if payload.get("execution_id") else None,
        cleaned_data_id=uuid.UUID(payload["cleaned_data_id"]) if payload.get("cleaned_data_id") else None,
        model=payload.get("model", "gpt-4o"),
        prompt_type=payload.get("prompt_type", "generate"),
        input_tokens=payload.get("input_tokens", 0),
        output_tokens=payload.get("output_tokens", 0),
        total_cost=payload.get("total_cost", 0),
        input_summary=payload.get("input_summary"),
        output_content=payload.get("output_content", ""),
    )
    db.add(ai)
    await db.commit()
    return {"received": True, "id": str(ai.id)}


@router.post("/trigger-workflow")
async def trigger_workflow(payload: dict):
    from app.config import settings
    import httpx

    url = f"{settings.N8N_WEBHOOK_URL}/webhook/ai-workflow-hub"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=30)
        return {"status": response.status_code, "response": response.json()}
