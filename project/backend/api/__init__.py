from fastapi import APIRouter
from . import auth, dashboard, executions, health, webhooks, sheets, ai, notify, rag, reports

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
router.include_router(executions.router, prefix="/executions", tags=["Executions"])
router.include_router(health.router, prefix="/health", tags=["Health"])
router.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])
router.include_router(sheets.router, prefix="/sheets", tags=["Google Sheets"])
router.include_router(ai.router, prefix="/ai", tags=["AI Processing"])
router.include_router(notify.router, prefix="/notify", tags=["Notifications"])
router.include_router(rag.router, prefix="/rag", tags=["RAG"])
router.include_router(reports.router, prefix="/reports", tags=["Reports"])
