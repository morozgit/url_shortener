from httpx import ASGITransport, AsyncClient
from db.db import get_async_session, Base
from src.main import app

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

import pytest


TEST_DB_URL = "postgresql+asyncpg://postgres:postgres@localhost/test_db"

# ----------------------------------------
# Function-scoped AsyncClient + session
# ----------------------------------------
@pytest.fixture
async def ac() -> AsyncGenerator[AsyncClient, None]:
    # создаём engine и sessionmaker для каждого теста
    engine = create_async_engine(TEST_DB_URL, future=True)
    SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

    # переопределяем зависимость FastAPI
    async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
        async with SessionLocal() as session:
            yield session

    app.dependency_overrides[get_async_session] = get_test_session

    # создаём/очищаем таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # создаём AsyncClient
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client

    await engine.dispose()