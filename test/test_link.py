from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_add_link(ac: AsyncClient):
    response = await ac.post("/link", json={"original_url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data
    assert len(data["short_url"]) == 6


@pytest.mark.asyncio
async def test_add_link_invalid_url(ac: AsyncClient):
    response = await ac.post("/link", json={"original_url": "not-a-url"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_redirect(ac: AsyncClient):
    res1 = await ac.post("/link", json={"original_url": "https://example.com"})
    short_url = res1.json()["short_url"]

    res2 = await ac.get(f"/link/{short_url}")
    assert res2.status_code == 200
    data = res2.json()
    assert data["original_url"] == "https://example.com/"


@pytest.mark.asyncio
async def test_redirect_not_found(ac: AsyncClient):
    response = await ac.get("/link/UNKNOWN")
    assert response.status_code == 404
    assert response.json()["detail"] == "Link not found"