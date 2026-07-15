from .data_fetcher import DataFetcher
from .ai_service import AIService
from .notification_service import NotificationService
from .data_processor import DataProcessor
from .sheets_service import SheetsService
from .report_service import ReportService

data_fetcher = DataFetcher()
ai_service = AIService()
notification_service = NotificationService()
data_processor = DataProcessor()
sheets_service = SheetsService()
report_service = ReportService()

__all__ = [
    "data_fetcher",
    "ai_service",
    "notification_service",
    "data_processor",
    "sheets_service",
    "report_service",
]
