---
name: fastapi
description: FastAPI conventions with Pydantic (2024-2026)
---

# FastAPI Conventions (FastAPI 0.100+)

## Core Principles

- **Type hints everywhere**
- **Pydantic for validation**
- **Async by default**
- **OpenAPI auto-generation**

## Project Structure

```
app/
  __init__.py
  main.py              # FastAPI app
  config.py            # Settings
  dependencies.py      # Shared deps
  api/
    __init__.py
    v1/
      __init__.py
      router.py        # API routes
      endpoints/
        users.py
        items.py
  models/              # SQLAlchemy/DB models
    user.py
  schemas/             # Pydantic schemas
    user.py
  services/            # Business logic
    user.py
  repositories/        # Data access
    user.py
tests/
```

## Schemas (Pydantic v2)

```python
from pydantic import BaseModel, Field, ConfigDict

class UserBase(BaseModel):
    email: str
    name: str | None = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
```

## Endpoints

```python
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
) -> User:
    user = await user_service.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> User:
    return await user_service.create(db, user_in)
```

## Dependencies

```python
from typing import Annotated
from fastapi import Depends

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)],
) -> User:
    # Validate token, get user
    ...

CurrentUser = Annotated[User, Depends(get_current_user)]

# Usage
@router.get("/me")
async def get_me(user: CurrentUser) -> UserResponse:
    return user
```

## Error Handling

- Use `HTTPException` for HTTP errors
- Custom exception handlers for domain errors
- Pydantic `ValidationError` auto-handled

## Async Database

- SQLAlchemy 2.0 async
- `asyncpg` for PostgreSQL
- Repository pattern for data access

## Testing

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    response = await client.post(
        "/users/",
        json={"email": "test@example.com", "password": "secret"}
    )
    assert response.status_code == 201
```

## Tools

- Ruff for linting/formatting
- mypy for type checking
- pytest-asyncio for async tests

## Reference Docs

- FastAPI Docs: https://fastapi.tiangolo.com/
- Pydantic v2: https://docs.pydantic.dev/
- SQLAlchemy 2.0: https://docs.sqlalchemy.org/
