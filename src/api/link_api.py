from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import link_service
from db.db import get_async_session
from schemas.link_schema import LinkAdd, LinkAddResponse, LinkStatsResponse
from services.link_service import LinkService

router = APIRouter(
    prefix="/link",
    tags=["URL"],
)


@router.post("")
async def add_link(
    link: LinkAdd,
    link_service: Annotated[LinkService, Depends(link_service)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> LinkAddResponse:
    short_link = await link_service.add_link(link, session)
    return LinkAddResponse(short_url=short_link)


@router.get("/{short_id}")
async def redirect(
    short_id: str,
    link_service: Annotated[LinkService, Depends(link_service)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> LinkAdd:
    original = await link_service.get_original(short_id, session)
    if not original:
        raise HTTPException(status_code=404, detail="Link not found")
    return LinkAdd(original_url=original)


@router.get("/stats/{short_code}")
async def link_stats(
    short_code: str,
    link_service: Annotated[LinkService, Depends(link_service)],
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> LinkStatsResponse:
    clicks = await link_service.get_stats(short_code, session)
    if clicks is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return LinkStatsResponse(clicks=clicks)