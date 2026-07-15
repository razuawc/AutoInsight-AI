import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
from database.session import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="SET NULL"))
    channel = Column(String(50), nullable=False)
    notification_type = Column(String(100))
    recipient = Column(String(255))
    subject = Column(String(500))
    body = Column(Text)
    sent_status = Column(String(50))
    sent_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class DeadLetterQueue(Base):
    __tablename__ = "dead_letter_queue"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="SET NULL"))
    source = Column(String(100), nullable=False)
    endpoint = Column(String(500))
    request_payload = Column(JSONB)
    error_type = Column(String(100))
    error_message = Column(Text)
    retry_count = Column(Integer, default=0)
    max_retries_reached = Column(Boolean, default=False)
    failed_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    resolved_at = Column(DateTime(timezone=True))
