# API Documentation

## Base URL

All endpoints are prefixed with `/api/v1`.

## Authentication

### Register
```http
POST /api/v1/auth/register?username=john&email=john@example.com&password=secret123
```

### Get Token
```http
POST /api/v1/auth/token
Content-Type: application/x-www-form-urlencoded

username=john&password=secret123
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

Use the token in subsequent requests:
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

## Dashboard

### Get Stats
```http
GET /api/v1/dashboard/stats
```

### Get Execution Timeline
```http
GET /api/v1/dashboard/execution-timeline?limit=50
```

## Executions

### List Executions
```http
GET /api/v1/executions?skip=0&limit=50
```

### Get Execution Details
```http
GET /api/v1/executions/{execution_id}
```

### Create Execution
```http
POST /api/v1/executions
Content-Type: application/json

{
  "workflow_name": "Manual Trigger",
  "trigger_type": "api"
}
```

## AI Processing

### Summarize
```http
POST /api/v1/ai/summarize?content=Your text to summarize here
```

### Extract Insights
```http
POST /api/v1/ai/insights?content=Your data here
```

### Classify
```http
POST /api/v1/ai/classify?content=Some content&categories=tech&categories=business&categories=science
```

### Recommendations
```http
POST /api/v1/ai/recommendations?content=Your data here
```

### Business Report
```http
POST /api/v1/ai/report?data_summary=Summary here&data_sources=News&data_sources=Weather
```

### Trends
```http
POST /api/v1/ai/trends?content=Your data here
```

## Health Checks

### Basic Health
```http
GET /api/v1/health/
```

### All Services
```http
GET /api/v1/health/all
```

### Individual
```http
GET /api/v1/health/database
GET /api/v1/health/redis
GET /api/v1/health/n8n
GET /api/v1/health/openai
```

## Notifications

### Slack
```http
POST /api/v1/notify/slack?message=Hello from AI Hub
```

### Email
```http
POST /api/v1/notify/email?to=user@example.com&subject=Report&body=<h1>Report</h1>
```

### Telegram
```http
POST /api/v1/notify/telegram?message=Alert!
```

## Google Sheets

### Append Row
```http
POST /api/v1/sheets/append?row=["2024-01-01","News","Summary","Insights","completed"]
```

### Get Sheet Data
```http
GET /api/v1/sheets/data
```

## Webhooks

### Workflow Completed
```http
POST /api/v1/webhooks/n8n/workflow-completed
Content-Type: application/json

{
  "execution_id": "uuid",
  "workflow_name": "Daily Aggregation",
  "status": "completed",
  "duration_ms": 15000
}
```

### Trigger Workflow
```http
POST /api/v1/webhooks/trigger-workflow
Content-Type: application/json

{
  "source": "manual"
}
```

## RAG

### Query
```http
POST /api/v1/rag/query?question=What trends were detected?
```

### Create Embedding
```http
POST /api/v1/rag/embed?text=Text to embed
```

## Reports

### Download PDF
```http
GET /api/v1/reports/pdf
```

### Download CSV
```http
GET /api/v1/reports/csv
```
