# FastAPI Starter (CRUD + JWT + SQLAlchemy + Alembic)

A small, production-style FastAPI starter includes:
- FastAPI + Uvicorn
- SQLAlchemy 2.x
- SQLite by default (switch to Postgres easily)
- Alembic migrations
- JWT login
- CRUD example (`items`)
- Pytest tests

## Quickstart

### 1) Create venv + install
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
# .venv\Scripts\activate

pip install -r requirements.txt
