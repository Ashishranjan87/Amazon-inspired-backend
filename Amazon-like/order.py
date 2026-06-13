from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from db.session import AsyncSessionLocal
from models.order import Order, OrderItem
from models.product import Product
from core.dependency import get_current_user
from models.user import User


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


def order_summary(order):
    return {
        "order_id": order.id,
        "user_id": order.user_id,
        "total_amount": order.total_amount,
        "status": order.status,
        "payment_id": order.payment_id,
    }


async def get_order_with_items(db, order_id: int, user_id: int):
    result = await db.execute(
        select(Order).where(
            Order.id == order_id,
            Order.user_id == user_id,
        )
    )
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    result = await db.execute(
        select(OrderItem, Product).join(
            Product,
            Product.id == OrderItem.product_id,
        ).where(
            OrderItem.order_id == order.id,
        )
    )

    items = []
    for order_item, product in result.all():
        items.append({
            "product_id": product.id,
            "product_name": product.name,
            "quantity": order_item.quantity,
            "price": order_item.price,
            "subtotal": order_item.price * order_item.quantity,
        })

    response = order_summary(order)
    response["items"] = items
    return response


@router.get("/")
async def get_orders(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(
            Order.user_id == current_user.id,
        ).order_by(Order.id.desc())
    )
    orders = result.scalars().all()
    return [order_summary(order) for order in orders]


@router.get("/{order_id}")
async def get_order(order_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await get_order_with_items(db, order_id, current_user.id)


@router.post("/{order_id}/cancel")
async def cancel_order(order_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(
            Order.id == order_id,
            Order.user_id == current_user.id,
        ).with_for_update()
    )
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    cancellable_statuses = {"pending_payment", "payment_failed"}
    if order.status not in cancellable_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Order cannot be cancelled while status is {order.status}",
        )

    order.status = "cancelled"
    await db.commit()
    await db.refresh(order)

    return {
        "message": "Order cancelled",
        "order": order_summary(order),
    }
