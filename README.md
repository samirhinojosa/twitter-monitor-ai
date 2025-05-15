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

## Project Structure
    .
    ├── api                     # FastAPI entry point
    ├── test                    # Automated tests
    ├── utils                   # Config, helpers
    ├── Dockerfile
    ├── README.md
    ├── pyproject.toml
    ├── README.md
    └── start.sh                # Start app (reloads in dev mode)

## Running the Project (Development)

```bash
docker build -t twitter-monitor-ai .
docker run -p 8000:8000 -e ENV=dev twitter-monitor-ai
```
Access the app at http://localhost:8000