-- ============================================================
-- AI Workflow Automation Hub - Database Initialization
-- ============================================================

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================
-- Users Table
-- ============================================================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);

-- ============================================================
-- Workflow Executions Table
-- ============================================================
CREATE TABLE IF NOT EXISTS workflow_executions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    n8n_workflow_id VARCHAR(100),
    n8n_execution_id VARCHAR(100),
    workflow_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    trigger_type VARCHAR(50),
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    duration_ms BIGINT,
    error_message TEXT,
    retry_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_executions_status ON workflow_executions(status);
CREATE INDEX idx_executions_created ON workflow_executions(created_at DESC);
CREATE INDEX idx_executions_workflow_name ON workflow_executions(workflow_name);

-- ============================================================
-- Raw API Responses
-- ============================================================
CREATE TABLE IF NOT EXISTS raw_api_responses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE CASCADE,
    source VARCHAR(100) NOT NULL,
    endpoint VARCHAR(500),
    request_params JSONB,
    response_body JSONB,
    status_code INTEGER,
    fetched_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_raw_source ON raw_api_responses(source);
CREATE INDEX idx_raw_execution ON raw_api_responses(execution_id);

-- ============================================================
-- Cleaned Data
-- ============================================================
CREATE TABLE IF NOT EXISTS cleaned_data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE CASCADE,
    raw_response_id UUID REFERENCES raw_api_responses(id) ON DELETE SET NULL,
    source VARCHAR(100) NOT NULL,
    data_type VARCHAR(100),
    cleaned_content JSONB NOT NULL,
    validation_status VARCHAR(50) DEFAULT 'pending',
    validation_errors JSONB,
    processed_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_cleaned_source ON cleaned_data(source);
CREATE INDEX idx_cleaned_execution ON cleaned_data(execution_id);

-- ============================================================
-- AI Outputs Table
-- ============================================================
CREATE TABLE IF NOT EXISTS ai_outputs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE CASCADE,
    cleaned_data_id UUID REFERENCES cleaned_data(id) ON DELETE SET NULL,
    model VARCHAR(100) DEFAULT 'gpt-4o',
    prompt_type VARCHAR(100) NOT NULL,
    input_tokens INTEGER DEFAULT 0,
    output_tokens INTEGER DEFAULT 0,
    total_cost DECIMAL(10,6) DEFAULT 0,
    input_summary TEXT,
    output_content TEXT NOT NULL,
    generated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_ai_execution ON ai_outputs(execution_id);
CREATE INDEX idx_ai_prompt_type ON ai_outputs(prompt_type);

-- ============================================================
-- Google Sheets Sync Log
-- ============================================================
CREATE TABLE IF NOT EXISTS sheets_sync_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE SET NULL,
    spreadsheet_id VARCHAR(255),
    sheet_name VARCHAR(100),
    rows_appended INTEGER DEFAULT 0,
    sync_status VARCHAR(50),
    error_message TEXT,
    synced_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- Notifications Log
-- ============================================================
CREATE TABLE IF NOT EXISTS notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE SET NULL,
    channel VARCHAR(50) NOT NULL,
    notification_type VARCHAR(100),
    recipient VARCHAR(255),
    subject VARCHAR(500),
    body TEXT,
    sent_status VARCHAR(50),
    sent_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_notif_channel ON notifications(channel);
CREATE INDEX idx_notif_execution ON notifications(execution_id);

-- ============================================================
-- Dead Letter Queue (Failed Requests)
-- ============================================================
CREATE TABLE IF NOT EXISTS dead_letter_queue (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    execution_id UUID REFERENCES workflow_executions(id) ON DELETE SET NULL,
    source VARCHAR(100) NOT NULL,
    endpoint VARCHAR(500),
    request_payload JSONB,
    error_type VARCHAR(100),
    error_message TEXT,
    retry_count INTEGER DEFAULT 0,
    max_retries_reached BOOLEAN DEFAULT FALSE,
    failed_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ
);

CREATE INDEX idx_dlq_source ON dead_letter_queue(source);
CREATE INDEX idx_dlq_resolved ON dead_letter_queue(resolved_at);

-- ============================================================
-- API Health Log
-- ============================================================
CREATE TABLE IF NOT EXISTS api_health_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    api_name VARCHAR(100) NOT NULL,
    endpoint VARCHAR(500),
    status_code INTEGER,
    response_time_ms INTEGER,
    is_healthy BOOLEAN,
    error_message TEXT,
    checked_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_health_api ON api_health_log(api_name);
CREATE INDEX idx_health_time ON api_health_log(checked_at DESC);

-- ============================================================
-- System Configuration
-- ============================================================
CREATE TABLE IF NOT EXISTS system_config (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    config_key VARCHAR(100) UNIQUE NOT NULL,
    config_value JSONB NOT NULL,
    description TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- Vector Store (for RAG)
-- ============================================================
CREATE TABLE IF NOT EXISTS vector_embeddings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source VARCHAR(100),
    content TEXT NOT NULL,
    embedding vector(1536),
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================
-- Default Configurations
-- ============================================================
INSERT INTO system_config (config_key, config_value, description) VALUES
('api_endpoints', '{
    "news_api": "https://newsapi.org/v2/top-headlines",
    "weather_api": "https://api.openweathermap.org/data/2.5/weather",
    "exchange_rate": "https://api.exchangerate-api.com/v4/latest/USD",
    "github_trending": "https://api.github.com/search/repositories"
}', 'Configured API endpoints for data fetching'),
('ai_prompts', '{
    "summarize": "Summarize the following data concisely:",
    "insights": "Extract key insights and trends from:",
    "classify": "Classify the following content into categories:",
    "recommend": "Generate actionable recommendations based on:"
}', 'AI prompt templates'),
('schedule_config', '{"time": "09:00", "timezone": "UTC"}', 'Workflow schedule configuration')
ON CONFLICT (config_key) DO NOTHING;
