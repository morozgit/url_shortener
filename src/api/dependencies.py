from repositories.link import LinkRepository
from services.link_service import LinkService
from db.db import async_session_maker


def link_service():
    return LinkService(LinkRepository())