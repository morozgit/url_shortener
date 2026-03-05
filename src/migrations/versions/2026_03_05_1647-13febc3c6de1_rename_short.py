"""rename short

Revision ID: 13febc3c6de1
Revises: d0ef8c32e6f5
Create Date: 2026-03-05 16:47:59.183013

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "13febc3c6de1"
down_revision: Union[str, Sequence[str], None] = "d0ef8c32e6f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("links", sa.Column("short_url", sa.String(length=10), nullable=False))
    op.drop_index(op.f("ix_links_short_id"), table_name="links")
    op.create_index(op.f("ix_links_short_url"), "links", ["short_url"], unique=True)
    op.drop_column("links", "short_id")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "links",
        sa.Column(
            "short_id", sa.VARCHAR(length=10), autoincrement=False, nullable=False
        ),
    )
    op.drop_index(op.f("ix_links_short_url"), table_name="links")
    op.create_index(op.f("ix_links_short_id"), "links", ["short_id"], unique=True)
    op.drop_column("links", "short_url")
