"""add link

Revision ID: d0ef8c32e6f5
Revises: 
Create Date: 2026-03-05 14:09:10.428446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0ef8c32e6f5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=2048), nullable=False),
    sa.Column('short_id', sa.String(length=10), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_links_short_id'), 'links', ['short_id'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_links_short_id'), table_name='links')
    op.drop_table('links')
