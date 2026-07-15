from fastapi import APIRouter, Depends
from services.notification_service import NotificationService
from app.config import settings

router = APIRouter()
notifier = NotificationService()


@router.post("/slack")
async def send_slack(message: str):
    success = await notifier.send_slack(message)
    return {"success": success, "channel": "slack"}


@router.post("/email")
async def send_email(to: str, subject: str, body: str):
    success = await notifier.send_email(to, subject, body)
    return {"success": success, "channel": "email", "to": to}


@router.post("/telegram")
async def send_telegram(message: str):
    success = await notifier.send_telegram(message)
    return {"success": success, "channel": "telegram"}
