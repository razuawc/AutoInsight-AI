import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, BigInteger, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from database.session import Base


class WorkflowExecution(Base):
    __tablename__ = "workflow_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    n8n_workflow_id = Column(String(100))
    n8n_execution_id = Column(String(100))
    workflow_name = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    trigger_type = Column(String(50))
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    duration_ms = Column(BigInteger)
    error_message = Column(Text)
    retry_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class RawAPIResponse(Base):
    __tablename__ = "raw_api_responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="CASCADE"))
    source = Column(String(100), nullable=False)
    endpoint = Column(String(500))
    request_params = Column(JSONB)
    response_body = Column(JSONB)
    status_code = Column(Integer)
    fetched_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class CleanedData(Base):
    __tablename__ = "cleaned_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="CASCADE"))
    raw_response_id = Column(UUID(as_uuid=True), ForeignKey("raw_api_responses.id", ondelete="SET NULL"))
    source = Column(String(100), nullable=False)
    data_type = Column(String(100))
    cleaned_content = Column(JSONB, nullable=False)
    validation_status = Column(String(50), default="pending")
    validation_errors = Column(JSONB)
    processed_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class AIOutput(Base):
    __tablename__ = "ai_outputs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("workflow_executions.id", ondelete="CASCADE"))
    cleaned_data_id = Column(UUID(as_uuid=True), ForeignKey("cleaned_data.id", ondelete="SET NULL"))
    model = Column(String(100), default="gpt-4o")
    prompt_type = Column(String(100), nullable=False)
    input_tokens = Column(Integer, default=0)
    output_tokens = Column(Integer, default=0)
    total_cost = Column(Integer, default=0)
    input_summary = Column(Text)
    output_content = Column(Text, nullable=False)
    generated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
