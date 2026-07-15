#!/bin/bash
# Database backup script
set -e

BACKUP_DIR=${BACKUP_DIR:-./backups}
DB_HOST=${DB_HOST:-localhost}
DB_PORT=${DB_PORT:-5432}
DB_USER=${DB_USER:-aihub}
DB_NAME=${DB_NAME:-ai_workflow_hub}
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/aihub_${TIMESTAMP}.sql.gz"

mkdir -p "${BACKUP_DIR}"

echo "Backing up database ${DB_NAME} to ${BACKUP_FILE}..."
PGPASSWORD="${DB_PASSWORD}" pg_dump -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" "${DB_NAME}" | gzip > "${BACKUP_FILE}"

echo "Backup completed: ${BACKUP_FILE}"
echo "Size: $(du -h "${BACKUP_FILE}" | cut -f1)"

# Keep only last 7 days of backups
find "${BACKUP_DIR}" -name "aihub_*.sql.gz" -mtime +7 -delete
