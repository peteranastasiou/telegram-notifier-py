FROM python:3.12-slim

# Read required arguments
ARG PUSHOVER_APIKEY
RUN test -n "$PUSHOVER_APIKEY"
ENV PUSHOVER_APIKEY $PUSHOVER_APIKEY

ARG PUSHOVER_USERKEY
RUN test -n "$PUSHOVER_USERKEY"
ENV PUSHOVER_USERKEY $PUSHOVER_USERKEY

# Setup and install
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app .

# Don't run as root
RUN useradd appuser && chown -R appuser /app
USER appuser

# Run
CMD ["fastapi", "run", "main.py", "--port", "80"]
