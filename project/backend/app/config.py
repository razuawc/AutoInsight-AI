from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Workflow Automation Hub"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://aihub:aihub_secret@localhost:5432/ai_workflow_hub"
    DATABASE_SYNC_URL: Optional[str] = None

    # Redis
    REDIS_URL: str = "redis://:redis_secret@localhost:6379/0"

    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o"
    OPENAI_MAX_TOKENS: int = 2000
    OPENAI_TEMPERATURE: float = 0.7

    # JWT
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Slack
    SLACK_WEBHOOK_URL: Optional[str] = None

    # Gmail
    GMAIL_USER: Optional[str] = None
    GMAIL_APP_PASSWORD: Optional[str] = None

    # Google Sheets
    GOOGLE_SHEETS_CREDENTIALS: str = "{}"
    GOOGLE_SHEETS_SPREADSHEET_ID: Optional[str] = None

    # n8n
    N8N_WEBHOOK_URL: str = "http://localhost:5678"
    N8N_API_KEY: Optional[str] = None

    # CORS
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:8000"

    # Telegram
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    TELEGRAM_CHAT_ID: Optional[str] = None

    # Sentry
    SENTRY_DSN: Optional[str] = None

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
