# AI Software Factory

Autonomous software engineering orchestration platform.

The project documentation in `docs/` is the source of truth for architecture and
implementation order.

## Backend Foundation

Install backend dependencies:

```powershell
python -m pip install -e ".[dev]"
```

Run backend tests:

```powershell
python -m pytest
```

Run backend lint:

```powershell
python -m ruff check app tests
```

Start the API locally:

```powershell
python -m uvicorn app.main:app --reload
```

The API health endpoint is available at:

```text
GET /health
```
