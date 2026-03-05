import random
import string
from repositories.link import LinkRepository
from schemas.link_schema import LinkAdd


class LinkService:

    def __init__(self, repo: LinkRepository):
        self.repo = repo

    def _generate_code(self, length: int = 6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    async def add_link(self, link: LinkAdd, session) -> str:
        short_url = self._generate_code()
        await self.repo.add_one({
            "original_url": str(link.original_url),
            "short_url": short_url
        }, session)
        return short_url

    async def get_original(self, short_id: str, session):
        link = await self.repo.get_and_increment(short_id, session)
        if link:
            return link.original_url
        return None

    async def get_stats(self, short_id: str, session):
        link = await self.repo.get_stats(short_id, session)
        if link:
            return link.clicks
        return None