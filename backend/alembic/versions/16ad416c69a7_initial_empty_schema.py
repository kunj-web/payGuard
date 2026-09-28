"""initial empty schema

Revision ID: 16ad416c69a7
Revises: 7918f4bf2fd4
Create Date: 2026-09-28 23:21:01.187419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16ad416c69a7'
down_revision: Union[str, Sequence[str], None] = '7918f4bf2fd4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
