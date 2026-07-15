#!/bin/bash
# Deployment script for AI Workflow Automation Hub
set -e

echo "========================================"
echo "AI Workflow Automation Hub - Deployment"
echo "========================================"

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "docker-compose is required but not installed."; exit 1; }

# Check .env file
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your configuration values."
    exit 1
fi

echo "Building and starting services..."
docker-compose build --parallel
docker-compose up -d

echo "Waiting for services to be healthy..."
sleep 10

echo "Running database migrations..."
docker-compose exec backend alembic upgrade head

echo ""
echo "========================================"
echo "Deployment completed successfully!"
echo "========================================"
echo ""
echo "Access points:"
echo "  FastAPI Docs:   http://localhost:8000/docs"
echo "  n8n Editor:     http://localhost:5678"
echo "  Grafana:        http://localhost:3000 (admin/admin)"
echo "  Prometheus:     http://localhost:9090"
echo "  pgAdmin:        http://localhost:5050 (admin@aihub.com/admin)"
echo ""
echo "Monitor logs with: docker-compose logs -f"
echo "Stop with:         docker-compose down"
