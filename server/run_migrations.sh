#!/bin/bash

# Exit on error
set -e

echo "Creating database if it doesn't exist..."
python create_db.py

echo "Running database migrations..."

# Run database migrations
alembic upgrade head

echo "Migrations completed successfully"

# Initialize database with initial data
echo "Initializing database with initial data..."
python init_db.py

echo "Database setup completed successfully" 