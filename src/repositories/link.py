from sqlalchemy import insert, select, update
from models.link import LinkOrm
from db.db import async_session_maker


class LinkRepository:

    async def add_one(self, data: dict, session):
        stmt = insert(LinkOrm).values(**data).returning(LinkOrm)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one()

    async def get_and_increment(self, short_url: str, session):
        result = await session.execute(
            select(LinkOrm).filter_by(short_url=short_url)
        )
        link = result.scalar_one_or_none()
        if link:
            await session.execute(
                update(LinkOrm)
                .where(LinkOrm.short_url == short_url)
                .values(clicks=LinkOrm.clicks + 1)
            )
        return link

    async def get_stats(self, short_url: str, session):
        result = await session.execute(
            select(LinkOrm).filter_by(short_url=short_url)
        )
        return result.scalar_one_or_none()