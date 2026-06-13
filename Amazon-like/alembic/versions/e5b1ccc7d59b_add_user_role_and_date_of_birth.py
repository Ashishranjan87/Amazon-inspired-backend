"""add user role and date of birth

Revision ID: e5b1ccc7d59b
Revises: 91b8c2a7e4f0
Create Date: 2026-06-05 10:19:04.775987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5b1ccc7d59b'
down_revision: Union[str, Sequence[str], None] = '91b8c2a7e4f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("user", sa.Column("date_of_birth", sa.Date(), nullable=True))
    op.add_column("user", sa.Column("role", sa.String(), nullable=True))
    op.execute("UPDATE \"user\" SET role = 'user' WHERE role IS NULL")
    op.alter_column("user", "role", nullable=False, server_default="user")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user", "role")
    op.drop_column("user", "date_of_birth")
