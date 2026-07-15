import json
from typing import Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.config import settings


class SheetsService:
    def __init__(self):
        self.service = None
        self._init_service()

    def _init_service(self):
        try:
            creds_info = json.loads(settings.GOOGLE_SHEETS_CREDENTIALS)
            if creds_info:
                creds = service_account.Credentials.from_service_account_info(creds_info)
                self.service = build("sheets", "v4", credentials=creds)
        except (json.JSONDecodeError, Exception):
            self.service = None

    async def append_row(self, row: list[str], spreadsheet_id: Optional[str] = None, sheet_name: str = "Sheet1") -> bool:
        if not self.service:
            return False
        sid = spreadsheet_id or settings.GOOGLE_SHEETS_SPREADSHEET_ID
        if not sid:
            return False
        try:
            body = {"values": [row]}
            result = self.service.spreadsheets().values().append(
                spreadsheetId=sid,
                range=sheet_name,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body=body,
            ).execute()
            return result.get("updates", {}).get("updatedRows", 0) > 0
        except Exception:
            return False

    async def append_summary_row(self, date: str, source: str, summary: str, insights: str, status: str) -> bool:
        return await self.append_row([date, source, summary, insights, status])

    async def get_sheet_data(self, spreadsheet_id: Optional[str] = None, range: str = "Sheet1!A:E") -> list:
        if not self.service:
            return []
        sid = spreadsheet_id or settings.GOOGLE_SHEETS_SPREADSHEET_ID
        if not sid:
            return []
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=sid, range=range).execute()
            return result.get("values", [])
        except Exception:
            return []
