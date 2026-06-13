"""add payment fields to orders

Revision ID: 3a6d3c93d7f2
Revises: create_orders_and_order_items
Create Date: 2026-06-04 00:00:00.000000
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "3a6d3c93d7f2"
down_revision: Union[str, Sequence[str], None] = "create_orders_and_order_items"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("orders", sa.Column("payment_id", sa.String(), nullable=True))
    op.add_column("order_items", sa.Column("price", sa.Float(), nullable=True))


def downgrade() -> None:
    op.drop_column("order_items", "price")
    op.drop_column("orders", "payment_id")
