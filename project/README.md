# AI Workflow Automation Hub

A production-ready AI-powered data aggregation and automation platform built with n8n, FastAPI, PostgreSQL, Redis, and OpenAI.

## Architecture

```
                    ┌─────────────┐
                    │   Grafana   │
                    │  (Monitor)  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Prometheus │
                    │  (Metrics)  │
                    └──────┬──────┘
                           │
┌──────────┐    ┌──────────▼──────────┐    ┌──────────┐
│  n8n     │◄──►│   FastAPI Backend   │◄──►│PostgreSQL│
│(Workflow)│    │   (API + AI + DB)   │    │  (Data)  │
└────┬─────┘    └──────────┬──────────┘    └──────────┘
     │                     │
     │              ┌──────▼──────┐
     │              │    Redis    │
     │              │  (Cache/Q)  │
     │              └─────────────┘
     │
     ├──► News API
     ├──► Weather API
     ├──► Exchange Rate API
     ├──► GitHub API
     └──► RSS Feeds
```

## Features

### Core
- **Scheduled Triggers**: Cron-based daily execution at 9:00 AM + manual + webhook
- **Data Fetching**: News, Weather, Exchange Rates, GitHub Trending, RSS Feeds
- **AI Processing**: Summaries, insights, trends, classification, recommendations, reports via GPT-4o
- **Data Pipeline**: Merge, deduplicate, validate, clean, normalize, transform
- **Database Storage**: Raw responses, cleaned data, AI outputs, execution logs, errors

### Integrations
- **Google Sheets**: Auto-append daily summaries
- **Gmail**: Email reports with AI summaries and CSV attachments
- **Slack**: Workflow start/complete/error notifications
- **Telegram Bot**: Real-time alerts (optional)
- **Google Sheets**: Bi-directional sync

### Monitoring & Observability
- **Grafana**: Pre-configured dashboards for executions, latencies, error rates
- **Prometheus**: Metrics collection with alerting rules
- **Health Checks**: All services (DB, Redis, n8n, OpenAI)
- **Prometheus Metrics**: FastAPI auto-instrumentation

### Security
- JWT authentication with OAuth2
- Password hashing (bcrypt)
- Rate limiting
- Environment-based secrets
- CORS configuration

### Error Handling
- Retry logic with exponential backoff (tenacity)
- Dead Letter Queue for failed requests
- Detailed execution logging
- Error notifications via Slack/Telegram

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Workflow Engine | n8n |
| API Backend | FastAPI (Python 3.12) |
| Database | PostgreSQL 16 |
| Cache/Queue | Redis 7 |
| AI | OpenAI GPT-4o / text-embedding-3-small |
| Monitoring | Grafana + Prometheus |
| Containers | Docker Compose |
| CI/CD | GitHub Actions |
| Auth | JWT + OAuth2 |

## Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key
- (Optional) News API key, Weather API key

### 1. Clone & Configure

```bash
git clone <repo-url> project
cd project
cp .env.example .env
```

### 2. Set Environment Variables

Edit `.env` with your keys:

```env
OPENAI_API_KEY=sk-...
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
GMAIL_USER=your@gmail.com
GMAIL_APP_PASSWORD=...
GOOGLE_SHEETS_CREDENTIALS='{...}'
```

### 3. Deploy

```bash
docker-compose build
docker-compose up -d
```

### 4. Access Services

| Service | URL | Credentials |
|---------|-----|-------------|
| FastAPI Docs | http://localhost:8000/docs | - |
| n8n Editor | http://localhost:5678 | Set in n8n setup |
| Grafana | http://localhost:3000 | admin / admin |
| Prometheus | http://localhost:9090 | - |
| pgAdmin | http://localhost:5050 | admin@aihub.com / admin |

### 5. Import n8n Workflow

1. Open n8n at http://localhost:5678
2. Go to **Workflows** > **Import from File**
3. Select `n8n/workflows/ai-workflow-hub.json`
4. Configure credentials (OpenAI, HTTP Request nodes)
5. Activate the workflow

## API Endpoints

### Dashboard
- `GET /api/v1/dashboard/stats` — execution statistics
- `GET /api/v1/dashboard/execution-timeline` — recent executions

### Executions
- `GET /api/v1/executions` — list executions
- `GET /api/v1/executions/{id}` — execution details
- `POST /api/v1/executions` — create execution

### AI Processing
- `POST /api/v1/ai/summarize` — generate summary
- `POST /api/v1/ai/insights` — extract insights
- `POST /api/v1/ai/classify` — classify data
- `POST /api/v1/ai/recommendations` — generate recommendations
- `POST /api/v1/ai/report` — business report
- `POST /api/v1/ai/trends` — detect trends

### Health
- `GET /api/v1/health/` — basic health
- `GET /api/v1/health/all` — all services health
- `GET /api/v1/health/database` — DB health
- `GET /api/v1/health/redis` — Redis health
- `GET /api/v1/health/n8n` — n8n health

### Notifications
- `POST /api/v1/notify/slack` — send Slack message
- `POST /api/v1/notify/email` — send email
- `POST /api/v1/notify/telegram` — send Telegram

### RAG
- `POST /api/v1/rag/query` — query with context
- `POST /api/v1/rag/embed` — create embedding

### Reports
- `GET /api/v1/reports/pdf` — download PDF report
- `GET /api/v1/reports/csv` — download CSV export

### Auth
- `POST /api/v1/auth/token` — get JWT token
- `POST /api/v1/auth/register` — register user

## Project Structure

```
project/
├── docker-compose.yml          # All services orchestration
├── .env.example                # Environment template
│
├── n8n/
│   ├── workflows/              # n8n workflow JSON exports
│   ├── credentials/            # n8n credential files
│   └── custom-nodes/           # Custom n8n nodes
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py             # FastAPI app entry point
│   │   └── config.py           # Settings
│   ├── api/                    # Route handlers
│   ├── database/               # DB session, CRUD
│   ├── models/                 # SQLAlchemy models
│   ├── services/               # Business logic
│   └── utils/                  # Security, logging, rate limiter
│
├── monitoring/
│   ├── prometheus/             # Scrape config, alerts
│   └── grafana/                # Dashboards, datasources
│
├── scripts/
│   ├── init-db.sql             # Schema initialization
│   ├── deploy.sh               # Deployment script
│   └── backup.sh               # DB backup script
│
├── docs/                       # API docs
└── .github/workflows/          # CI/CD pipeline
```

## Database Schema

- `users` — Authentication
- `workflow_executions` — Execution tracking
- `raw_api_responses` — Raw API data
- `cleaned_data` — Processed data
- `ai_outputs` — AI-generated content
- `notifications` — Sent notification log
- `sheets_sync_log` — Google Sheets sync log
- `dead_letter_queue` — Failed request queue
- `api_health_log` — Health check history
- `system_config` — Dynamic configuration
- `vector_embeddings` — RAG embeddings

## Monitoring

Grafana is pre-configured with:
- Prometheus datasource
- PostgreSQL datasource
- Execution overview dashboard
- API latency tracking
- Error rate monitoring

Alerts (via Prometheus):
- Backend service down
- High HTTP error rate (>10%)
- High workflow failure rate (>20%)
- Slow API responses (>2s p95)
- Database connection pool exhaustion

## CI/CD

GitHub Actions pipeline:
1. **Lint** — Ruff + MyPy
2. **Test** — pytest with PostgreSQL service
3. **Build & Push** — Docker images to GHCR
4. **Deploy** — SSH deployment to production

## Bonus Features

- **RAG Pipeline**: Query past AI outputs with context-aware answers
- **Vector Embeddings**: OpenAI text-embedding-3-small support
- **Telegram Bot**: Real-time workflow notifications
- **PDF Reports**: Auto-generated daily PDF reports
- **CSV Export**: Download execution data as CSV
- **Multi-User Auth**: JWT-based authentication with roles
- **Webhook Trigger**: REST API to trigger workflows remotely

## License

MIT
