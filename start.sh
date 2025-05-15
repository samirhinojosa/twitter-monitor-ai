#!/bin/sh

echo "Starting app in $ENV mode..."

# Default command to start FastAPI with Uvicorn
if [ "$ENV" = "dev"]; then
    # option: --reload only in development
    uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload
else
    uvicorn app.api.main:app --host 0.0.0.0 --port 8000
fi