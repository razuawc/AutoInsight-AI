from app.config import settings
import httpx


class TelegramBot:
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    async def send_message(self, chat_id: str, text: str) -> bool:
        if not self.token:
            return False
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sendMessage",
                json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"},
            )
            return response.status_code == 200

    async def send_document(self, chat_id: str, file_path: str) -> bool:
        if not self.token:
            return False
        async with httpx.AsyncClient() as client:
            with open(file_path, "rb") as f:
                response = await client.post(
                    f"{self.base_url}/sendDocument",
                    data={"chat_id": chat_id},
                    files={"document": f},
                )
                return response.status_code == 200

    async def set_webhook(self, url: str) -> bool:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/setWebhook",
                json={"url": url},
            )
            return response.status_code == 200
