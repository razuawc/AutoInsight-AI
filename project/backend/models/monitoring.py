import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from database.session import Base


class APIHealthLog(Base):
    __tablename__ = "api_health_log"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    api_name = Column(String(100), nullable=False)
    endpoint = Column(String(500))
    status_code = Column(Integer)
    response_time_ms = Column(Integer)
    is_healthy = Column(Boolean)
    error_message = Column(Text)
    checked_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class SystemConfig(Base):
    __tablename__ = "system_config"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    config_key = Column(String(100), unique=True, nullable=False)
    config_value = Column(JSONB, nullable=False)
    description = Column(Text)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
