from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from services.report_service import ReportService
from services.ai_service import AIService
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from database.session import get_db
from models.execution import AIOutput, WorkflowExecution
from app.config import settings
from datetime import datetime
import tempfile
import os

router = APIRouter()
report_service = ReportService()
ai_service = AIService()


@router.get("/pdf")
async def generate_pdf_report(db: AsyncSession = Depends(get_db)):
    ai_result = await db.execute(
        select(AIOutput).order_by(desc(AIOutput.generated_at)).limit(5)
    )
    ai_outputs = ai_result.scalars().all()

    exec_result = await db.execute(
        select(WorkflowExecution).order_by(desc(WorkflowExecution.created_at)).limit(100)
    )
    executions = exec_result.scalars().all()

    total = len(executions)
    completed = sum(1 for e in executions if e.status == "completed")
    failed = sum(1 for e in executions if e.status == "failed")

    data = {
        "generated_at": datetime.utcnow().isoformat(),
        "summary": "AI Workflow Automation Hub - Automated Report",
        "insights": [
            f"{total} total workflow executions processed",
            f"{completed} completed successfully ({round(completed/total*100,1)}% success rate)" if total else "0 executions",
            f"{failed} failed executions",
            f"{len(ai_outputs)} AI analyses performed",
        ],
        "recommendations": [
            "Monitor API health endpoints regularly",
            "Review DLQ for recurring failures",
            "Optimize AI prompts for better summaries",
        ],
        "metrics": {
            "Total Executions": total,
            "Success Rate": f"{round(completed/total*100,1)}%" if total else "N/A",
            "Failed": failed,
            "AI Outputs": len(ai_outputs),
        },
    }

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    report_service.generate_pdf_report(data, tmp.name)
    tmp.close()

    return FileResponse(
        tmp.name,
        media_type="application/pdf",
        filename=f"aihub-report-{datetime.now().strftime('%Y%m%d')}.pdf",
    )


@router.get("/csv")
async def generate_csv_report(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(WorkflowExecution).order_by(desc(WorkflowExecution.created_at)).limit(1000)
    )
    executions = result.scalars().all()

    data = []
    for e in executions:
        data.append({
            "id": str(e.id),
            "workflow": e.workflow_name,
            "status": e.status,
            "trigger": e.trigger_type,
            "duration_ms": e.duration_ms,
            "error": e.error_message or "",
            "created_at": e.created_at.isoformat() if e.created_at else "",
        })

    headers = ["id", "workflow", "status", "trigger", "duration_ms", "error", "created_at"]
    csv_content = report_service.generate_csv(data, headers)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="w")
    tmp.write(csv_content)
    tmp.close()

    return FileResponse(
        tmp.name,
        media_type="text/csv",
        filename=f"aihub-executions-{datetime.now().strftime('%Y%m%d')}.csv",
    )
