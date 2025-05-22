# Twitter Monitor AI

An intelligent daily Twitter (now X) monitoring system that checks specific accounts for content related to a specific topic (even in images), and sends alerts via email and SMS. 

## 🚀 Project Goals

- Monitor specific Twitter (now X) accounts daily
- Use NLP and OCR to detect topics in tweets and images
- Notify via email and SMS if relevant content is found
- Fully containerized and cloud-deployable

## Technologies Used
- Poetry
- Docker
- FastAPI
- Tweepy

## Project Structure
    .
    ├── api                     # FastAPI entry point
    ├── core                    # Core application settings (config, environment, logging)
    ├── domain
        ├── domain              # Domain models/entities        
        ├── schemas             # Pydantic models used for request/response serialization (DTOs)     
    ├── infrastructure
        ├── repositories        # Concrete implementations of data access (e.g., DB, cache)
        ├── services            # Third-party integrations (e.g., Twitter API via Tweepy, ML, etc.)
    ├── interfaces              # Abstract interfaces (ports) for external dependencies like APIs, DBs
    ├── use_cases               # Application-specific business logic (orchestration layer)
    ├── test                    # Unit and integration tests
    ├── Dockerfile
    ├── LICENSE
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    └── start.sh                # Shell script to launch the app (with dev reload using uvicorn)

## Running the Project (Development)

```bash
docker build -t twitter-monitor-ai .

# Executing in dev mode
docker run -e ENV=dev -e PORT=8000 -p 8000:8000 -v $(pwd):/app twitter-monitor-ai
```
Access the app at http://localhost:8000