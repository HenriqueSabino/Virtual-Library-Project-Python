#!/bin/sh

# Wait for the database to become available
echo "Waiting for the database to become available..."
while ! nc -z ${DB_HOST} ${DB_PORT}; do   
  sleep 1
done
echo "Database is available."

# Apply database migrations
echo "Applying database migrations..."
alembic upgrade head

# Start the application
echo "Starting the application..."
exec "$@"