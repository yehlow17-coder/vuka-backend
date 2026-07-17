# VUKA Backend

Production-ready FastAPI backend for the VUKA VPN mobile application.

## Features

- Async FastAPI application with clean layered architecture
- SQLAlchemy models for configs, countries, networks, deployments, announcements, and app versions
- Pydantic schemas for request/response validation
- Service and repository layers for business logic
- Alembic-ready migration setup for PostgreSQL
- Environment-driven configuration for later Render and PostgreSQL deployment
- Working FastAPI entrypoint with CORS and health endpoint

## Structure

- `app/api` — API routes and dependencies
- `app/services` — business logic services
- `app/repositories` — persistence access layer
- `app/models` — SQLAlchemy ORM models
- `app/schemas` — request/response validation models
- `app/config` — environment settings
- `app/database` — database session and base models

## Quick start

1. Create a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in the required values.
4. Start the API from the `backend` folder:
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Notes

- PostgreSQL support is ready, but the app does not connect to a database until `DATABASE_URL` is provided.
- This backend is structured for Render deployment and can be wired to environment variables later.
