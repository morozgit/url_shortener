from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class LinkOrm(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    short_url: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    clicks: Mapped[int] = mapped_column(Integer, default=0, nullable=False)