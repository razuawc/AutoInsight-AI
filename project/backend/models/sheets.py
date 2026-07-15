import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database.session import Base


class SheetsSyncLog(Base):
    __tablename__ = "sheets_sync_log"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="SET NULL"))
    spreadsheet_id = Column(String(255))
    sheet_name = Column(String(100))
    rows_appended = Column(Integer, default=0)
    sync_status = Column(String(50))
    error_message = Column(Text)
    synced_at = Column(DateTime(timezone=True), default=datetime.utcnow)
