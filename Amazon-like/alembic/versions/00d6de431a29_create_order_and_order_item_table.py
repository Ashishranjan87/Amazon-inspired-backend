from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = "create_orders_and_order_items"
down_revision = "7dfacb8c8748"   # ⚠️ change this if you already have migrations
branch_labels = None
depends_on = None


def upgrade():
    # ✅ Orders table
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("total_amount", sa.Float(), nullable=False),
        sa.Column("status", sa.String(), nullable=True, server_default="pending"),
    )

    # ✅ Order Items table
    op.create_table(
        "order_items",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("order_id", sa.Integer(), sa.ForeignKey("orders.id"), nullable=False),
        sa.Column("product_id", sa.Integer(), sa.ForeignKey("product.id"), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
    )


def downgrade():
    op.drop_table("order_items")
    op.drop_table("orders")