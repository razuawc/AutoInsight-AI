from app.config import settings
from typing import Optional
import httpx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class NotificationService:
    async def send_slack(self, message: str, webhook_url: Optional[str] = None) -> bool:
        url = webhook_url or settings.SLACK_WEBHOOK_URL
        if not url:
            return False
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"text": message})
            return response.status_code == 200

    async def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        attachment_path: Optional[str] = None,
    ) -> bool:
        if not settings.GMAIL_USER or not settings.GMAIL_APP_PASSWORD:
            return False

        msg = MIMEMultipart()
        msg["From"] = settings.GMAIL_USER
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))

        if attachment_path:
            with open(attachment_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={attachment_path.split('/')[-1]}")
                msg.attach(part)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(settings.GMAIL_USER, settings.GMAIL_APP_PASSWORD)
            server.send_message(msg)
        return True

    async def send_telegram(self, message: str) -> bool:
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            return False
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"chat_id": settings.TELEGRAM_CHAT_ID, "text": message})
            return response.status_code == 200

    async def notify_workflow_started(self, workflow_name: str) -> None:
        msg = f"Workflow '{workflow_name}' started execution."
        await self.send_slack(msg)
        await self.send_telegram(msg)

    async def notify_workflow_completed(self, workflow_name: str, status: str, duration_ms: int) -> None:
        msg = f"Workflow '{workflow_name}' completed with status: {status} (Duration: {duration_ms}ms)"
        await self.send_slack(msg)

    async def notify_workflow_error(self, workflow_name: str, error: str) -> None:
        msg = f"Workflow '{workflow_name}' failed with error: {error}"
        await self.send_slack(msg)
        await self.send_telegram(msg)
