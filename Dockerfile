FROM python:3.12-slim

# Set environment variables
ENV POETRY_VERSION=2.1.3 
ENV POETRY_HOME="/opt/poetry" 
ENV PATH="$POETRY_HOME/bin:$PATH" 
ENV PYTHONUNBUFFERED=1

# Install system-level dependencies and Tesseract OCR
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    curl \
    build-essential \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*    

# Install Poetry using its official install script
RUN curl -sSL https://install.python-poetry.org | python3 \
    && ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry     

# Set the working directory for the app
WORKDIR /app

# Copy Poetry config and dependencies files
COPY pyproject.toml poetry.lock ./

# Install Python dependencies using Poetry (without creating a virtualenv)
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --no-interaction --no-ansi

# Copy source code into the container
COPY app ./app

# Copy the start script
COPY start.sh ./
RUN chmod +x ./start.sh

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start app (reloads in dev mode)
CMD ["./start.sh"]