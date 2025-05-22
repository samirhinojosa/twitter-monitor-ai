# Project settings
APP_NAME=twitter-monitor-ai
APP_MODULE=app.main:app
POETRY=poetry


# Run the FastAPI app with Uvicorn
run:
	@$(POETRY) run uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port 8000

# Run the FastAPI app with Uvicorn (option: --reload only in development)
run-dev:
	@$(POETRY) run uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port 8000 --reload --reload-dir /app

# Install dependencies
install:
	@$(POETRY) install

# Clean Python cache files
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} + && \
	find . -type f -name '*.pyc' -delete

# Build Docker image
docker-build:
	docker build -t $(APP_NAME):latest .

# Run Docker container
docker-run:
	docker run --rm -it -p 8000:8000 $(APP_NAME):latest

# Run Docker container in dev mode
docker-run-dev:
	docker run --rm -it \
		-e ENV=dev \
		-e PORT=8000 \
		-p 8000:8000 \
		-v $(shell pwd):/app \
		$(APP_NAME)

# Display help
help:
	@echo "Makefile commands:"
	@echo "  make run           	- Run the FastAPI app"
	@echo "  make run-dev           - Run the FastAPI app in dev mode"	
	@echo "  make install       	- Install dependencies via Poetry"
	@echo "  make clean         	- Remove __pycache__ and .pyc files"
	@echo "  make docker-build  	- Build Docker image"
	@echo "  make docker-run    	- Run app in Docker container"
	@echo "  make docker-run-dev    - Run app in Docker container in dev mode"	