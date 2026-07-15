<div align="center">

# 🤖 AutoInsight AI

### AI Workflow Automation Hub

**A production-ready, AI-powered data aggregation and automation platform that orchestrates intelligent workflows — from data ingestion to AI analysis to automated reporting.**

[![GitHub Stars](https://img.shields.io/github/stars/razuawc/AutoInsight-AI?style=flat-square&logo=github&label=Stars)](https://github.com/razuawc/AutoInsight-AI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/razuawc/AutoInsight-AI?style=flat-square&logo=github&label=Forks)](https://github.com/razuawc/AutoInsight-AI/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/razuawc/AutoInsight-AI?style=flat-square&logo=github&label=Issues)](https://github.com/razuawc/AutoInsight-AI/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1.svg?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/features/actions)

<br>

[🚀 Quick Start](#-quick-start) • [📖 API Docs](#-api-documentation) • [🏗️ Architecture](#%EF%B8%8F-architecture) • [📊 Monitoring](#-monitoring) • [🗺️ Roadmap](#%EF%B8%8F-roadmap)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Architecture](#%EF%B8%8F-architecture)
- [Folder Structure](#-folder-structure)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [API Documentation](#-api-documentation)
- [Database](#-database)
- [Authentication](#-authentication)
- [User Roles](#-user-roles)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Performance](#-performance)
- [Security](#-security)
- [Monitoring](#-monitoring)
- [Roadmap](#%EF%B8%8F-roadmap)
- [Contributing](#-contributing)
- [Coding Standards](#-coding-standards)
- [Changelog](#-changelog)
- [FAQ](#-faq)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Author](#-author)
- [Support](#-support)
- [Acknowledgements](#-acknowledgements)

---

## ✨ Features

### 🔄 Core Automation
| Feature | Description |
|---------|-------------|
| **Scheduled Triggers** | Cron-based daily execution (9:00 AM) + manual + webhook triggers |
| **Data Fetching** | News, Weather, Exchange Rates, GitHub Trending — all automated |
| **AI Processing** | Summaries, insights, trends, classification, recommendations via GPT-4o |
| **Data Pipeline** | Merge, deduplicate, validate, clean, normalize, transform |
| **Database Storage** | Raw responses, cleaned data, AI outputs, execution logs, errors |

### 🔌 Integrations
| Integration | Description |
|-------------|-------------|
| **Google Sheets** | Auto-append daily summaries and insights |
| **Gmail** | Email reports with AI summaries and CSV attachments |
| **Slack** | Workflow start, completion, and error notifications |
| **Telegram Bot** | Real-time alerts and document delivery |
| **n8n** | Visual workflow orchestration engine |

### 📊 Monitoring & Observability
- **Grafana** — Pre-configured dashboards (executions, latencies, error rates)
- **Prometheus** — Metrics collection with 5 alerting rules
- **Health Checks** — Deep checks for DB, Redis, n8n, OpenAI
- **FastAPI Instrumentation** — Auto-generated Prometheus metrics

### 🛡️ Security
- JWT authentication with OAuth2
- bcrypt password hashing
- Per-IP rate limiting
- Environment-based secrets
- CORS configuration

### ⚠️ Error Handling
- Retry logic with exponential backoff (tenacity)
- Dead Letter Queue for failed requests
- Detailed execution logging
- Error notifications via Slack/Telegram

---

## 📸 Screenshots

<div align="center">

| Grafana Dashboard | n8n Workflow | API Docs |
|:---:|:---:|:---:|
| ![Grafana Dashboard](https://via.placeholder.com/600x300/1a1a2e/00d2ff?text=Grafana+Dashboard) | ![n8n Workflow](https://via.placeholder.com/600x300/1a1a2e/ff6b6b?text=n8n+Workflow) | ![API Docs](https://via.placeholder.com/600x300/1a1a2e/ffd93d?text=Swagger+Docs) |

| Prometheus Alerts | pgAdmin | Telegram Bot |
|:---:|:---:|:---:|
| ![Prometheus](https://via.placeholder.com/600x300/1a1a2e/6bcb77?text=Prometheus+Alerts) | ![pgAdmin](https://via.placeholder.com/600x300/1a1a2e/4d96ff?text=pgAdmin) | ![Telegram](https://via.placeholder.com/600x300/1a1a2e/c084fc?text=Telegram+Bot) |

</div>

> 📌 *Replace placeholder URLs with actual screenshots by placing images in `docs/screenshots/`.*

---

## 🎯 Demo

| | URL |
|---|---|
| 🌐 **Frontend** | `http://localhost:5678` (n8n Editor) |
| ⚙️ **Backend API** | `http://localhost:8000/docs` (Swagger UI) |
| 📚 **Documentation** | `http://localhost:8000/redoc` (ReDoc) |
| 📊 **Grafana** | `http://localhost:3000` (admin / admin) |
| 🔍 **Prometheus** | `http://localhost:9090` |
| 🗄️ **pgAdmin** | `http://localhost:5050` (admin@aihub.com / admin) |

---

## 🧰 Tech Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Workflow Engine** | n8n | Latest | Visual workflow orchestration, scheduling, webhook triggers |
| **Backend API** | FastAPI | 0.115.0 | REST API, async request handling, auto-generated docs |
| **Language** | Python | 3.12 | Core runtime |
| **AI Engine** | OpenAI GPT-4o | — | Summaries, insights, classification, recommendations |
| **Vector Embeddings** | OpenAI text-embedding-3-small | — | RAG pipeline for context-aware queries |
| **Database** | PostgreSQL | 16 | Primary data store with JSONB, pgvector |
| **Cache / Queue** | Redis | 7 | Caching, rate limiting, Celery task queue |
| **ORM** | SQLAlchemy | 2.0.35 | Async database operations |
| **Migrations** | Alembic | 1.13.2 | Database schema versioning |
| **HTTP Client** | httpx | 0.27.2 | Async external API calls with retry |
| **Task Queue** | Celery | 5.4.0 | Background task processing |
| **Monitoring** | Grafana + Prometheus | — | Dashboards, metrics, alerting |
| **Containerization** | Docker + Docker Compose | — | Service orchestration |
| **Reverse Proxy** | Nginx | — | Routing, load balancing |
| **CI/CD** | GitHub Actions | — | Lint, test, build, deploy pipeline |
| **Package Registry** | GitHub Container Registry | — | Docker image storage |
| **Auth** | JWT + OAuth2 | — | Token-based authentication |
| **PDF Generation** | ReportLab | 4.2.2 | Auto-generated reports |
| **Email** | Gmail SMTP | — | Automated email reports |
| **Notifications** | Slack SDK, Telegram Bot | — | Multi-channel alerts |
| **Spreadsheet** | Google Sheets API | 2.142.0 | Data export |
| **Error Tracking** | Sentry | 2.14.0 | Production error monitoring |
| **Backoff / Retry** | Tenacity | 9.0.0 | Exponential retry logic |
| **Testing** | pytest | — | Unit and integration tests |
| **Linting** | Ruff + MyPy | — | Code quality, type safety |

---

## 🏗️ Architecture

### System Overview

AutoInsight AI follows a **microservices-inspired architecture** orchestrated via Docker Compose. The system is built around a central **FastAPI backend** that bridges an **n8n workflow engine** with **AI services**, **external APIs**, and **notification channels**.

### Request Flow

1. **Trigger** — n8n fires on schedule (cron), webhook, or manual click
2. **Fetch** — n8n pulls data from NewsAPI, OpenWeatherMap, ExchangeRate-API, GitHub API
3. **Process** — Data is merged, deduplicated, and cleaned via code nodes
4. **AI** — Processed data is sent to FastAPI → OpenAI GPT-4o for summarization and analysis
5. **Store** — All stages (raw, cleaned, AI output) are persisted to PostgreSQL
6. **Report** — Results are pushed to Google Sheets, emailed via Gmail, and notified on Slack/Telegram
7. **Monitor** — Prometheus scrapes metrics; Grafana visualizes and alerts

### Mermaid Diagram

```mermaid
graph TB
    subgraph Triggers["🎯 Triggers"]
        CRON["⏰ Cron Schedule<br/>Daily 9:00 AM"]
        WEBHOOK["🔗 Webhook<br/>REST API"]
        MANUAL["👆 Manual<br/>n8n UI"]
    end

    subgraph n8n["📦 n8n Workflow Engine"]
        N8N["n8n Orchestrator"]
        FETCH["📡 Data Fetchers<br/>News • Weather<br/>Exchange Rates • GitHub"]
        MERGE["🔀 Merge &<br/>Clean Data"]
        AI_NODE["🤖 AI Processing<br/>GPT-4o"]
    end

    subgraph Backend["⚡ FastAPI Backend"]
        API["REST API<br/>/api/v1/*"]
        AI_SVC["🧠 AI Service<br/>OpenAI GPT-4o"]
        RAG["📚 RAG Service<br/>Embeddings"]
        NOTIFY["🔔 Notification<br/>Service"]
        REPORT["📄 Report<br/>Service"]
    end

    subgraph Storage["💾 Storage"]
        PG[("🐘 PostgreSQL 16<br/>Primary DB")]
        REDIS[("🔴 Redis 7<br/>Cache & Queue")]
        LANCE["🔮 LanceDB<br/>Vector Store"]
    end

    subgraph External["🌍 External Services"]
        SLACK["💬 Slack"]
        EMAIL["📧 Gmail"]
        TELEGRAM["📱 Telegram"]
        SHEETS["📊 Google Sheets"]
        SENTRY["🐛 Sentry"]
    end

    subgraph Monitor["📊 Monitoring"]
        PROM["Prometheus<br/>Metrics"]
        GRAF["Grafana<br/>Dashboards"]
    end

    subgraph CI["🚀 CI/CD"]
        ACTIONS["GitHub Actions"]
        GHCR["GitHub Container<br/>Registry"]
    end

    CRON --> N8N
    WEBHOOK --> N8N
    MANUAL --> N8N

    N8N --> FETCH
    FETCH --> MERGE
    MERGE --> AI_NODE
    AI_NODE -->|POST /webhooks/n8n/ai-output| API

    API --> AI_SVC
    API --> RAG
    API --> NOTIFY
    API --> REPORT
    API --> PG
    API --> REDIS

    AI_SVC -->|OpenAI API| OPENAI{{"🌐 OpenAI<br/>GPT-4o"}}
    RAG --> LANCE
    RAG -->|OpenAI Embeddings| OPENAI

    NOTIFY --> SLACK
    NOTIFY --> EMAIL
    NOTIFY --> TELEGRAM
    NOTIFY --> SHEETS

    API --> SENTRY

    PG --> PROM
    API --> PROM
    PROM --> GRAF

    ACTIONS -->|Build & Push| GHCR
    ACTIONS -->|SSH Deploy| Backend

    style Triggers fill:#1a1a2e,stroke:#00d2ff,color:#fff
    style n8n fill:#1a1a2e,stroke:#ff6b6b,color:#fff
    style Backend fill:#1a1a2e,stroke:#6bcb77,color:#fff
    style Storage fill:#1a1a2e,stroke:#ffd93d,color:#fff
    style External fill:#1a1a2e,stroke:#c084fc,color:#fff
    style Monitor fill:#1a1a2e,stroke:#4d96ff,color:#fff
    style CI fill:#1a1a2e,stroke:#ff922b,color:#fff
```

---

## 📁 Folder Structure

```
AutoInsight-AI/
├── .gitignore
├── main.py                              # PyCharm placeholder
│
└── project/
    ├── docker-compose.yml               # Full stack orchestration (7 services)
    ├── .env.example                     # Environment variable template
    ├── .env                             # Secrets (git-ignored)
    │
    ├── backend/
    │   ├── Dockerfile                   # Python 3.12-slim + uvicorn
    │   ├── requirements.txt             # 31 Python dependencies
    │   ├── alembic.ini                  # Alembic configuration
    │   │
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── main.py                  # FastAPI app, lifespan, CORS, routers
    │   │   └── config.py                # Pydantic Settings (all env vars)
    │   │
    │   ├── api/
    │   │   ├── __init__.py              # Master router (/api/v1)
    │   │   ├── auth.py                  # POST /token, POST /register
    │   │   ├── dashboard.py             # GET /stats, /execution-timeline
    │   │   ├── executions.py            # CRUD workflow executions
    │   │   ├── ai.py                    # AI summarize, insights, classify, etc.
    │   │   ├── health.py                # Health checks (DB, Redis, n8n, OpenAI)
    │   │   ├── notify.py                # Slack, Email, Telegram
    │   │   ├── webhooks.py              # n8n webhook receivers
    │   │   ├── sheets.py                # Google Sheets integration
    │   │   ├── rag.py                   # RAG query + embedding
    │   │   └── reports.py               # PDF + CSV export
    │   │
    │   ├── models/
    │   │   ├── __init__.py              # Exports all models
    │   │   ├── user.py                  # User (auth, roles)
    │   │   ├── execution.py             # WorkflowExecution, RawAPIResponse, etc.
    │   │   ├── sheets.py                # SheetsSyncLog
    │   │   ├── notification.py          # Notification log
    │   │   └── monitoring.py            # APIHealthLog, DeadLetterQueue, SystemConfig
    │   │
    │   ├── database/
    │   │   ├── __init__.py
    │   │   ├── session.py               # Async SQLAlchemy engine + session
    │   │   ├── base_repo.py             # Generic BaseRepository
    │   │   └── crud.py                  # CRUDBase with dashboard stats
    │   │
    │   ├── services/
    │   │   ├── __init__.py              # Service singletons
    │   │   ├── ai_service.py            # OpenAI GPT-4o integration
    │   │   ├── data_fetcher.py          # httpx + tenacity retry
    │   │   ├── data_processor.py        # Merge, clean, transform
    │   │   ├── notification_service.py  # Slack, Email, Telegram
    │   │   ├── rag_service.py           # Embeddings + context retrieval
    │   │   ├── report_service.py        # ReportLab PDF + CSV
    │   │   ├── sheets_service.py        # Google Sheets API v4
    │   │   └── telegram_bot.py          # Telegram Bot API
    │   │
    │   ├── utils/
    │   │   ├── __init__.py
    │   │   ├── security.py              # JWT decode, API key verification
    │   │   ├── rate_limiter.py          # In-memory sliding window limiter
    │   │   └── logger.py                # Structured logging (DEBUG/INFO)
    │   │
    │   ├── alembic/
    │   │   ├── env.py                   # Async migration runner
    │   │   ├── script.py.mako           # Migration template
    │   │   └── versions/                # Migration scripts
    │   │
    │   └── tests/
    │       └── __init__.py              # Test suite (pytest)
    │
    ├── docker/
    │   ├── .dockerignore
    │   └── nginx.conf                   # Reverse proxy → backend, n8n, grafana
    │
    ├── monitoring/
    │   ├── prometheus/
    │   │   ├── prometheus.yml           # Scrape configs (5 targets)
    │   │   └── alerts.yml              # 5 alerting rules
    │   └── grafana/
    │       ├── datasources/
    │       │   └── datasources.yml      # Prometheus + PostgreSQL
    │       ├── dashboards/
    │       │   ├── dashboard.yml        # Provisioning config
    │       │   └── ai-workflow-hub.json # Pre-built dashboard (5 panels)
    │
    ├── n8n/
    │   └── workflows/
    │       └── ai-workflow-hub.json     # 17-node workflow definition
    │
    ├── scripts/
    │   ├── init-db.sql                  # Full schema DDL (11 tables)
    │   ├── deploy.sh                    # Build + deploy script
    │   └── backup.sh                    # Automated pg_dump rotation
    │
    ├── docs/
    │   └── api.md                       # Full API reference with examples
    │
    └── .github/
        └── workflows/
            └── ci.yml                   # Lint → Test → Build → Deploy
```

---

## ⚡ Installation

### Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Docker | 20.10+ | Latest |
| Docker Compose | 2.0+ | Latest |
| Python | 3.12 | 3.12+ |
| RAM | 4 GB | 8 GB+ |
| Disk | 2 GB | 5 GB+ |

### 🔑 Required API Keys

| Service | Purpose | Get Key |
|---------|---------|---------|
| OpenAI | AI processing (GPT-4o) | [platform.openai.com](https://platform.openai.com/api-keys) |
| NewsAPI | News aggregation | [newsapi.org](https://newsapi.org/register) |
| OpenWeatherMap | Weather data | [openweathermap.org](https://openweathermap.org/api) |
| Slack | Notifications | [Slack API](https://api.slack.com/messaging/webhooks) |
| Google Cloud | Sheets + Service Account | [console.cloud.google.com](https://console.cloud.google.com/) |
| Sentry *(optional)* | Error tracking | [sentry.io](https://sentry.io/) |
| Telegram *(optional)* | Bot alerts | [@BotFather](https://t.me/BotFather) |

### Clone Repository

```bash
git clone https://github.com/razuawc/AutoInsight-AI.git
cd AutoInsight-AI/project
```

### Backend Setup

```bash
# Create virtual environment (for local development)
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r backend/requirements.txt

# Run database migrations
alembic upgrade head
```

### Frontend Setup (n8n)

n8n runs as a Docker container — no separate frontend setup required. The n8n editor is accessible at `http://localhost:5678`.

### Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials:

```env
# ═══════════════════════════════════════
# 🗄️ DATABASE
# ═══════════════════════════════════════
DATABASE_URL=postgresql+asyncpg://aihub:aihub_secret@postgres:5432/aihub_db
DATABASE_SYNC_URL=postgresql://aihub:aihub_secret@postgres:5432/aihub_db

# ═══════════════════════════════════════
# 🔴 REDIS
# ═══════════════════════════════════════
REDIS_URL=redis://:redis_secret@redis:6379/0

# ═══════════════════════════════════════
# 🤖 OPENAI
# ═══════════════════════════════════════
OPENAI_API_KEY=sk-your-openai-api-key
OPENAI_MODEL=gpt-4o
OPENAI_MAX_TOKENS=2000
OPENAI_TEMPERATURE=0.7

# ═══════════════════════════════════════
# 🔐 SECURITY
# ═══════════════════════════════════════
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ═══════════════════════════════════════
# 📡 N8N
# ═══════════════════════════════════════
N8N_WEBHOOK_URL=http://n8n:5678/webhook
N8N_API_KEY=your-n8n-api-key

# ═══════════════════════════════════════
# 🔔 NOTIFICATIONS
# ═══════════════════════════════════════
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/xxx/xxx
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=your-chat-id

# ═══════════════════════════════════════
# 📊 GOOGLE SHEETS
# ═══════════════════════════════════════
GOOGLE_SHEETS_CREDENTIALS='{"type":"service_account",...}'
GOOGLE_SHEETS_SPREADSHEET_ID=your-spreadsheet-id

# ═══════════════════════════════════════
# 🌐 CORS & RATE LIMITING
# ═══════════════════════════════════════
CORS_ORIGINS=["http://localhost:3000","http://localhost:5678"]
RATE_LIMIT_PER_MINUTE=60

# ═══════════════════════════════════════
# 🐛 ERROR TRACKING (Optional)
# ═══════════════════════════════════════
SENTRY_DSN=https://your-sentry-dsn
```

---

## 🏃 Running the Project

### Development

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Backend hot-reload is enabled via volume mount
# Edit backend code → changes apply instantly
```

### Production

```bash
# Build optimized images
docker-compose build

# Start in detached mode
docker-compose up -d --remove-orphans

# Check service health
docker-compose ps
```

### Docker

```bash
# Build backend image only
docker build -t autoinsight-backend ./backend

# Run standalone
docker run -d \
  --name backend \
  -p 8000:8000 \
  --env-file .env \
  autoinsight-backend
```

### Docker Compose

| Command | Description |
|---------|-------------|
| `docker-compose up -d` | Start all services in background |
| `docker-compose down` | Stop all services |
| `docker-compose down -v` | Stop and remove all data (volumes) |
| `docker-compose logs -f [service]` | Tail logs for a specific service |
| `docker-compose ps` | List running services |
| `docker-compose build --no-cache` | Rebuild images from scratch |
| `docker-compose exec backend bash` | Shell into backend container |

### Services & Ports

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| 📡 FastAPI Backend | `http://localhost:8000` | — |
| 📖 Swagger UI | `http://localhost:8000/docs` | — |
| 📚 ReDoc | `http://localhost:8000/redoc` | — |
| 🔄 n8n Editor | `http://localhost:5678` | (set during n8n init) |
| 📊 Grafana | `http://localhost:3000` | admin / admin |
| 🔍 Prometheus | `http://localhost:9090` | — |
| 🗄️ pgAdmin | `http://localhost:5050` | admin@aihub.com / admin |

### Import n8n Workflow

```bash
# After starting services:
# 1. Open http://localhost:5678
# 2. Workflows → Import from File
# 3. Select: n8n/workflows/ai-workflow-hub.json
# 4. Configure credentials (OpenAI API key)
# 5. Click "Activate"
```

---

## 📖 API Documentation

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/auth/register` | Register a new user |
| `POST` | `/api/v1/auth/token` | Login and get JWT token |

### Dashboard

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/dashboard/stats` | Execution statistics & success rate |
| `GET` | `/api/v1/dashboard/execution-timeline` | Recent execution timeline |

### Executions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/executions` | List all executions (paginated) |
| `GET` | `/api/v1/executions/{id}` | Get execution details + AI output |
| `POST` | `/api/v1/executions` | Create a new execution |

### AI Processing

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/ai/summarize` | Generate AI summary |
| `POST` | `/api/v1/ai/insights` | Extract key insights |
| `POST` | `/api/v1/ai/classify` | Classify data by categories |
| `POST` | `/api/v1/ai/recommendations` | Generate recommendations |
| `POST` | `/api/v1/ai/report` | Full business report |
| `POST` | `/api/v1/ai/trends` | Detect data trends |

### Health Checks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/health/` | Basic health status |
| `GET` | `/api/v1/health/all` | All services aggregated |
| `GET` | `/api/v1/health/database` | PostgreSQL latency |
| `GET` | `/api/v1/health/redis` | Redis latency |
| `GET` | `/api/v1/health/n8n` | n8n availability |
| `GET` | `/api/v1/health/openai` | OpenAI API key validity |

### Notifications

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/notify/slack` | Send Slack message |
| `POST` | `/api/v1/notify/email` | Send email with optional attachment |
| `POST` | `/api/v1/notify/telegram` | Send Telegram message |

### Webhooks (n8n Integration)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/webhooks/n8n/workflow-completed` | Record completed execution |
| `POST` | `/api/v1/webhooks/n8n/data-fetched` | Store raw API response |
| `POST` | `/api/v1/webhooks/n8n/ai-output` | Store AI generation output |
| `POST` | `/api/v1/webhooks/trigger-workflow` | Trigger n8n workflow remotely |

### Integrations

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/sheets/append` | Append row to Google Sheets |
| `POST` | `/api/v1/sheets/append-summary` | Append summary with metadata |
| `GET` | `/api/v1/sheets/data` | Read sheet data |

### RAG (Retrieval-Augmented Generation)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/rag/query` | Context-aware AI query |
| `POST` | `/api/v1/rag/embed` | Create text embedding |

### Reports

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/reports/pdf` | Download PDF report |
| `GET` | `/api/v1/reports/csv` | Download CSV export |

> 📘 Full API reference with request/response examples: [`docs/api.md`](project/docs/api.md)

---

## 🗄️ Database

### Schema Overview

The database uses **PostgreSQL 16** with **asyncpg** for async operations and supports **JSONB** columns for flexible data storage.

| Table | Purpose | Key Relationships |
|-------|---------|-------------------|
| `users` | Authentication & roles | — |
| `workflow_executions` | Execution tracking | → users |
| `raw_api_responses` | Raw API data storage | → workflow_executions |
| `cleaned_data` | Processed & validated data | → workflow_executions, raw_api_responses |
| `ai_outputs` | AI-generated content | → workflow_executions, cleaned_data |
| `notifications` | Notification log | → workflow_executions |
| `dead_letter_queue` | Failed request queue | → workflow_executions |
| `sheets_sync_log` | Google Sheets sync log | → workflow_executions |
| `api_health_log` | Health check history | — |
| `system_config` | Dynamic configuration (JSONB) | — |
| `vector_embeddings` | RAG vector embeddings (pgvector) | — |

### Entity Relationship

```mermaid
erDiagram
    users ||--o{ workflow_executions : "creates"
    workflow_executions ||--o{ raw_api_responses : "fetches"
    workflow_executions ||--o{ cleaned_data : "processes"
    workflow_executions ||--o{ ai_outputs : "generates"
    workflow_executions ||--o{ notifications : "sends"
    workflow_executions ||--o{ dead_letter_queue : "fails"
    workflow_executions ||--o{ sheets_sync_log : "syncs"
    raw_api_responses ||--o{ cleaned_data : "cleans"
    cleaned_data ||--o{ ai_outputs : "analyzes"

    users {
        uuid id PK
        varchar email UK
        varchar username UK
        varchar hashed_password
        varchar full_name
        boolean is_active
        boolean is_superuser
        timestamp created_at
        timestamp updated_at
    }

    workflow_executions {
        uuid id PK
        varchar n8n_workflow_id
        varchar n8n_execution_id
        varchar workflow_name
        varchar status
        varchar trigger_type
        timestamp started_at
        timestamp completed_at
        integer duration_ms
        text error_message
        integer retry_count
    }

    raw_api_responses {
        uuid id PK
        uuid execution_id FK
        varchar source
        varchar endpoint
        jsonb request_params
        jsonb response_body
        integer status_code
        timestamp fetched_at
    }

    ai_outputs {
        uuid id PK
        uuid execution_id FK
        varchar model
        varchar prompt_type
        integer input_tokens
        integer output_tokens
        numeric total_cost
        text input_summary
        jsonb output_content
    }

    dead_letter_queue {
        uuid id PK
        uuid execution_id FK
        varchar source
        varchar error_type
        text error_message
        integer retry_count
        boolean max_retries_reached
    }
```

### Migrations

```bash
# Generate a new migration
alembic revision --autogenerate -m "description"

# Apply pending migrations
alembic upgrade head

# Rollback one step
alembic downgrade -1

# View current revision
alembic current
```

### Database Initialization

The `scripts/init-db.sql` script creates all tables with indexes and seeds default configuration:

```sql
-- API endpoint configurations
INSERT INTO system_config (config_key, config_value, description) VALUES
('api_endpoints', '{"news": "https://newsapi.org/v2/top-headlines", ...}', 'Configured API URLs');

-- AI prompt templates
INSERT INTO system_config (config_key, config_value, description) VALUES
('ai_prompts', '{"summarize": "Provide a concise summary...", ...}', 'AI prompt templates');

-- Schedule configuration
INSERT INTO system_config (config_key, config_value, description) VALUES
('schedule_config', '{"time": "09:00", "timezone": "UTC"}', 'Workflow schedule');
```

---

## 🔐 Authentication

### Login Flow

```
┌─────────┐     POST /auth/register     ┌─────────┐
│  Client  │ ──────────────────────────► │ Backend │
│          │ ◄────────────────────────── │         │
│          │     { user_id, email }      │         │
│          │                             │         │
│          │     POST /auth/token        │         │
│          │ ──────────────────────────► │         │
│          │     (username + password)   │         │
│          │ ◄────────────────────────── │         │
│          │     { access_token,         │         │
│          │       token_type }          │         │
│          │                             │         │
│          │     GET /api/v1/*           │         │
│          │ ──────────────────────────► │         │
│          │     Authorization: Bearer   │         │
│          │ ◄────────────────────────── │         │
└─────────┘     Protected response       └─────────┘
```

### JWT Configuration

| Parameter | Value |
|-----------|-------|
| Algorithm | HS256 |
| Token Expiry | 30 minutes |
| Payload | `sub` (user UUID), `username` |
| Secret | `SECRET_KEY` env variable |

### Password Hashing

- **Algorithm:** bcrypt via `passlib`
- **Library:** `passlib[bcrypt]` 1.7.4

### Refresh Token

> ⚠️ *Currently not implemented. Access tokens expire after 30 minutes. A refresh token mechanism is planned for the roadmap.*

### API Key Authentication

An additional `verify_api_key` utility is available for service-to-service authentication:

```python
from utils.security import verify_api_key

@router.get("/internal")
async def internal_endpoint(api_key: str = Depends(verify_api_key)):
    return {"message": "authenticated"}
```

---

## 👥 User Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full access: all endpoints, user management, system config, superuser operations |
| **Manager** | Read/write access: executions, AI, reports, sheets. No user management |
| **User** | Read-only: dashboard, execution history, reports. Limited AI queries |
| **Guest** | Public endpoints only: health checks, registration |

> 📌 *Role-based access control is partially implemented via `is_superuser` flag. Full RBAC is on the [Roadmap](#%EF%B8%8F-roadmap).*

---

## 🚀 Deployment

### Docker Deployment

```bash
# Production build
docker-compose -f docker-compose.yml build --no-cache

# Deploy all services
docker-compose -f docker-compose.yml up -d --remove-orphans

# Verify deployment
docker-compose ps
docker-compose logs --tail=50 backend
```

### Nginx Reverse Proxy

The `docker/nginx.conf` configures routing:

| Path | Service |
|------|---------|
| `/` | FastAPI Backend (port 8000) |
| `/n8n/` | n8n Editor (port 5678) |
| `/grafana/` | Grafana Dashboard (port 3000) |

### CI/CD — GitHub Actions

The pipeline runs **4 stages** on every push:

```yaml
# .github/workflows/ci.yml
Stage 1: lint        → Ruff + MyPy
Stage 2: test        → pytest with PostgreSQL service container
Stage 3: build-push  → Docker Buildx → GitHub Container Registry (GHCR)
Stage 4: deploy      → SSH deploy to production server
```

**Pipeline Flow:**

```
Push to main → Lint → Test → Build & Push to GHCR → Deploy via SSH
```

**Registry:** Images are pushed to `ghcr.io/razuawc/autoinsight-ai` with tags `latest` and `${{ github.sha }}`.

### Deployment Script

```bash
# Automated deployment
chmod +x scripts/deploy.sh
./scripts/deploy.sh

# What it does:
# 1. Checks Docker & Docker Compose
# 2. Builds all service images
# 3. Starts all services
# 4. Runs Alembic migrations
# 5. Prints access URLs
```

### Database Backup

```bash
# Manual backup
chmod +x scripts/backup.sh
./scripts/backup.sh

# What it does:
# 1. pg_dump with gzip compression
# 2. Stores in ./backups/ with timestamp
# 3. Auto-deletes backups older than 7 days
```

### Server Requirements

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 2 vCPUs | 4+ vCPUs |
| RAM | 4 GB | 8 GB+ |
| Storage | 20 GB SSD | 50 GB+ SSD |
| OS | Ubuntu 22.04+ | Ubuntu 24.04 LTS |
| Docker | 20.10+ | Latest |
| Ports | 8000, 5678, 3000, 9090, 5050, 5432, 6379 | All above + 80/443 |

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
cd backend
pytest tests/ -v

# Run with async support
pytest tests/ -v --asyncio-mode=auto

# Run with coverage
pytest tests/ -v --cov=. --cov-report=html

# Run specific test file
pytest tests/test_auth.py -v

# Run specific test
pytest tests/test_auth.py::test_login -v
```

### Test Structure

```
backend/tests/
├── __init__.py
├── conftest.py              # Fixtures, test DB setup
├── test_auth.py             # Authentication tests
├── test_executions.py       # Execution CRUD tests
├── test_ai.py               # AI endpoint tests
├── test_health.py           # Health check tests
└── test_webhooks.py         # Webhook integration tests
```

### CI Testing

Tests run automatically in CI with a PostgreSQL service container:

```yaml
services:
  postgres:
    image: postgres:16-alpine
    env:
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: test_password
      POSTGRES_DB: test_db
    ports:
      - 5432:5432
```

---

## ⚡ Performance

### Caching Strategy

| Layer | Tool | TTL | Purpose |
|-------|------|-----|---------|
| API Response Cache | Redis | 5 min | Cache frequently accessed endpoints |
| Rate Limiter | In-memory | 60s window | Prevent abuse (default 60 req/min) |
| Connection Pool | SQLAlchemy | Persistent | Pool size 20, overflow 10 |
| HTTP Client | httpx | Connection reuse | Max 10 concurrent connections |

### Optimizations

- **Async I/O** — All database and HTTP operations are fully async (`asyncpg`, `httpx`, `AsyncOpenAI`)
- **Connection Pooling** — SQLAlchemy pool: `pool_size=20`, `max_overflow=10`, `pool_pre_ping=True`
- **Retry with Backoff** — Tenacity retries with exponential backoff (2s–30s, 3 attempts)
- **Lazy Loading** — Services are singletons, initialized on first use
- **Pagination** — All list endpoints support `skip` and `limit` parameters
- **JSONB Storage** — Flexible schema for variable API responses without joins
- **Database Indexes** — Indexed on foreign keys, status columns, and timestamps

---

## 🛡️ Security

| Feature | Implementation |
|---------|---------------|
| **JWT Authentication** | `python-jose` with HS256, 30-minute expiry |
| **Password Hashing** | bcrypt via `passlib`, salt rounds auto |
| **HTTPS** | Nginx reverse proxy with TLS termination |
| **CORS** | Configurable origins via `CORS_ORIGINS` env |
| **Rate Limiting** | In-memory sliding window, per-IP, 60 req/min |
| **Input Validation** | Pydantic v2 models on all request/response payloads |
| **SQL Injection** | SQLAlchemy ORM — parameterized queries, no raw SQL |
| **XSS Protection** | JSON API responses only, Content-Type enforcement |
| **Secrets Management** | All secrets in `.env` files, never committed |
| **Error Tracking** | Sentry integration for production error monitoring |
| **Dead Letter Queue** | Failed requests captured for retry/analysis |
| **Docker Security** | Non-root user, minimal base image (`python:3.12-slim`) |

---

## 📊 Monitoring

### Prometheus Alerts

| Alert | Severity | Condition |
|-------|----------|-----------|
| `BackendDown` | 🔴 Critical | Backend service unreachable |
| `HighErrorRate` | 🟡 Warning | HTTP error rate > 10% |
| `ExecutionFailureRate` | 🟡 Warning | Workflow failure rate > 20% |
| `SlowResponses` | 🟡 Warning | p95 response time > 2 seconds |
| `DatabaseConnectionPoolExhausted` | 🔴 Critical | All DB connections in use |

### Grafana Dashboard Panels

| Panel | Type | Description |
|-------|------|-------------|
| Workflow Execution Status | Stat | Total executions + success/fail counts |
| API Response Times | Graph | p95 latency over time |
| HTTP Request Rate | Graph | Requests per second |
| Workflow Executions | Table | Recent execution history (SQL query) |
| Recent AI Outputs | Table | Latest AI generations (SQL query) |

### Prometheus Scrape Targets

| Target | Endpoint | Interval |
|--------|----------|----------|
| FastAPI Backend | `ai-backend:8000/metrics` | 15s |
| n8n | `n8n:5678/metrics` | 30s |
| PostgreSQL | `postgres:9187/metrics` | 30s |
| Redis | `redis:9121/metrics` | 30s |
| Prometheus Self | `prometheus:9090/metrics` | 15s |

---

## 🗺️ Roadmap

### v1.1 — Coming Soon

- [ ] 🔑 Refresh token mechanism
- [ ] 👥 Full RBAC (Admin / Manager / User / Guest)
- [ ] 🌐 Multi-language support (i18n)
- [ ] 📱 Mobile-responsive n8n dashboard wrapper

### v1.2 — Planned

- [ ] 🔄 WebSocket real-time execution updates
- [ ] 📈 Custom AI model fine-tuning pipeline
- [ ] 🗂️ File upload & document processing
- [ ] 🔗 More integrations: Notion, Airtable, HubSpot

### v2.0 — Future

- [ ] 🖥️ React/Next.js admin dashboard
- [ ] 🧩 Plugin system for custom workflow nodes
- [ ] 🌍 Multi-tenant support
- [ ] 📊 Advanced analytics dashboard
- [ ] 🤖 Multi-model AI support (Claude, Gemini, Llama)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

### 1. Fork & Clone

```bash
git clone https://github.com/your-username/AutoInsight-AI.git
cd AutoInsight-AI
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# Use prefixes: feature/, fix/, docs/, refactor/, test/
```

### 3. Set Up Development Environment

```bash
cd project
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
pip install ruff mypy pytest pytest-asyncio
```

### 4. Make Changes

- Write clean, documented code
- Follow the [Coding Standards](#-coding-standards)
- Add tests for new features
- Update documentation if needed

### 5. Lint & Test

```bash
# Lint
ruff check .
mypy backend/

# Test
pytest tests/ -v --asyncio-mode=auto
```

### 6. Commit

```bash
git add .
git commit -m "feat: add new feature description"
```

### 7. Push & Create PR

```bash
git push origin feature/your-feature-name
```

Open a Pull Request at [github.com/razuawc/AutoInsight-AI/pulls](https://github.com/razuawc/AutoInsight-AI/pulls)

### Contribution Guidelines

- 🐛 **Bug Reports** — Open an issue with steps to reproduce
- 💡 **Feature Requests** — Open an issue with use case
- 📖 **Documentation** — PRs improving docs are always welcome
- 🧪 **Tests** — Increasing coverage is encouraged

---

## 📏 Coding Standards

### Linting

```bash
# Ruff (linter + formatter)
ruff check .                    # Check for issues
ruff check --fix .              # Auto-fix issues
ruff format .                   # Format code

# MyPy (type checking)
mypy backend/ --ignore-missing-imports
```

### Code Style

| Rule | Standard |
|------|----------|
| **Formatter** | Ruff (Black-compatible) |
| **Linter** | Ruff |
| **Type Checker** | MyPy |
| **Line Length** | 88 characters |
| **Quotes** | Double quotes for strings |
| **Imports** | Sorted by Ruff (isort-compatible) |

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat:     New feature
fix:      Bug fix
docs:     Documentation only
style:    Code style (formatting, no logic change)
refactor: Code refactor (no feature/fix)
test:     Adding or updating tests
chore:    Build, CI, or tooling changes
perf:     Performance improvement
```

**Examples:**
```bash
feat: add Telegram bot integration
fix: resolve database connection pool leak
docs: update API endpoint documentation
test: add auth endpoint tests
chore: update Docker base image to Python 3.12
```

---

## 📋 Changelog

### v1.0.0 — Initial Release 🎉

**Backend**
- FastAPI application with async architecture
- PostgreSQL database with SQLAlchemy ORM
- Alembic migration system
- JWT authentication (OAuth2 flow)
- Rate limiting middleware

**AI Integration**
- OpenAI GPT-4o for summarization, insights, classification
- RAG pipeline with vector embeddings
- Structured JSON response support

**Workflow Automation**
- n8n workflow with 17 nodes
- Cron, webhook, and manual triggers
- Multi-source data fetching (News, Weather, Exchange Rates, GitHub)

**Integrations**
- Google Sheets auto-append
- Gmail email reports
- Slack notifications
- Telegram bot alerts

**Monitoring**
- Grafana dashboard (5 panels)
- Prometheus metrics + 5 alerting rules
- Health checks for all services

**DevOps**
- Docker Compose (7 services)
- GitHub Actions CI/CD (4 stages)
- Automated database backup
- Nginx reverse proxy

**Reporting**
- PDF report generation (ReportLab)
- CSV data export

---

## ❓ FAQ

### General

<details>
<summary><strong>What is AutoInsight AI?</strong></summary>

AutoInsight AI is an AI-powered automation platform that aggregates data from multiple sources (news, weather, exchange rates, GitHub trending), processes it through AI models (GPT-4o), and delivers insights via reports, dashboards, and notifications.
</details>

<details>
<summary><strong>Do I need an OpenAI API key?</strong></summary>

Yes. The core AI features (summarization, insights, classification) require an OpenAI API key. Get one at [platform.openai.com](https://platform.openai.com/api-keys).
</details>

<details>
<summary><strong>Can I run without n8n?</strong></summary>

Yes. The FastAPI backend works independently. n8n is optional for workflow automation and scheduling. You can trigger workflows via REST API webhooks instead.
</details>

### Technical

<details>
<summary><strong>Why async PostgreSQL?</strong></summary>

We use `asyncpg` with SQLAlchemy's async engine for non-blocking database operations, which significantly improves throughput under concurrent requests — critical for an API handling multiple webhook calls simultaneously.
</details>

<details>
<summary><strong>What is the Dead Letter Queue?</strong></summary>

Failed requests (API calls, notifications, etc.) are stored in the `dead_letter_queue` table with error details and retry count. This allows manual inspection, retry, or debugging without data loss.
</details>

<details>
<summary><strong>How does RAG work?</strong></summary>

Past AI outputs are embedded using OpenAI's `text-embedding-3-small` model and stored. When a query comes in, relevant context is retrieved and fed to GPT-4o for context-aware responses.
</details>

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `Connection refused` on PostgreSQL | Container not started | `docker-compose up -d postgres` and wait 10s |
| `Authentication failed` for OpenAI | Invalid API key | Verify `OPENAI_API_KEY` in `.env` |
| n8n workflow fails | Missing credentials | Configure OpenAI credentials in n8n UI |
| `rate limit exceeded` | Too many requests | Increase `RATE_LIMIT_PER_MINUTE` in `.env` |
| Grafana shows "No data" | Prometheus not scraping | Check `prometheus.yml` targets, restart Prometheus |
| `ModuleNotFoundError` in backend | Missing dependencies | `pip install -r backend/requirements.txt` |
| Docker build fails | Out of space | Run `docker system prune -a` |
| Email not sending | Gmail 2FA | Use App Password, not account password |

### Debug Commands

```bash
# Check service status
docker-compose ps

# View backend logs
docker-compose logs -f backend

# Check database connectivity
docker-compose exec postgres psql -U aihub -d aihub_db -c "\dt"

# Test Redis
docker-compose exec redis redis-cli -a redis_secret ping

# Verify OpenAI key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Check all health endpoints
curl http://localhost:8000/api/v1/health/all
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 razuawc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## 👨‍💻 Author

<table>
<tr>
<td align="center">
<a href="https://github.com/razuawc">
<img src="https://github.com/razuawc.png" width="100px;" alt=""/>
<br />
<sub><b>razuawc</b></sub>
</a>
<br />

[![Portfolio](https://img.shields.io/badge/🌐-Portfolio-00d2ff?style=flat-square)](YOUR_PORTFOLIO_URL)
[![LinkedIn](https://img.shields.io/badge/💼-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](YOUR_LINKEDIN_URL)
[![Email](https://img.shields.io/badge/📧-Email-D14836?style=flat-square&logo=mail&logoColor=white)](mailto:YOUR_EMAIL)
[![GitHub](https://img.shields.io/badge/🐙-GitHub-333?style=flat-square&logo=github&logoColor=white)](https://github.com/razuawc)

</td>
</tr>
</table>

---

## 💬 Support

If you need help or have questions:

| Channel | Link |
|---------|------|
| 🐛 **Bug Reports** | [GitHub Issues](https://github.com/razuawc/AutoInsight-AI/issues) |
| 💡 **Feature Requests** | [GitHub Discussions](https://github.com/razuawc/AutoInsight-AI/discussions) |
| 📧 **Email** | YOUR_EMAIL |
| 💼 **LinkedIn** | YOUR_LINKEDIN |

---

## 🙏 Acknowledgements

### Libraries & Frameworks

| Library | Purpose |
|---------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | High-performance async web framework |
| [SQLAlchemy](https://www.sqlalchemy.org/) | Database ORM and query builder |
| [Alembic](https://alembic.sqlalchemy.org/) | Database migration tool |
| [Pydantic](https://docs.pydantic.dev/) | Data validation and settings |
| [OpenAI Python SDK](https://github.com/openai/openai-python) | GPT-4o and embeddings API |
| [n8n](https://n8n.io/) | Workflow automation platform |
| [httpx](https://www.python-httpx.org/) | Async HTTP client |
| [Tenacity](https://tenacity.readthedocs.io/) | Retry logic with backoff |
| [ReportLab](https://www.reportlab.com/) | PDF report generation |
| [python-jose](https://python-jose.readthedocs.io/) | JWT token handling |
| [Slack SDK](https://api.slack.com/) | Slack integration |
| [Telegram Bot API](https://core.telegram.org/bots) | Telegram notifications |
| [Prometheus](https://prometheus.io/) | Metrics collection |
| [Grafana](https://grafana.com/) | Monitoring dashboards |
| [Docker](https://www.docker.com/) | Containerization |
| [GitHub Actions](https://github.com/features/actions) | CI/CD automation |

### Inspiration

- [n8n Community Workflows](https://n8n.io/workflows/)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-production-blueprint)
- [Full Stack FastAPI + PostgreSQL](https://fastapi.tiangolo.com/tutorial/sql-databases/)

---

<div align="center">

**Made with ❤️ by [razuawc](https://github.com/razuawc)**

⭐ Star this repo if you find it useful!

</div>
