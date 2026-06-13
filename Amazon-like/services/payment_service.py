from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from models.order import Order, OrderItem
from models.product import Product


async def process_payment(db, payment,user_id:int):
    result = await db.execute(
        select(Order).where(
            Order.id == payment.order_id,
            Order.user_id == user_id,
        ).with_for_update()
    )
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    if order.status == "paid":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order is already paid",
        )

    payable_statuses = {"pending_payment", "payment_failed"}
    if order.status not in payable_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Order cannot be paid while status is {order.status}",
        )

    if round(order.total_amount, 2) != round(payment.amount, 2):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Payment amount does not match order total",
        )

    if not payment.payment_token.startswith("tok_"):
        order.status = "payment_failed"
        await db.commit()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid payment token",
        )

    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order.id))
    order_items = result.scalars().all()

    for item in order_items:
        result = await db.execute(
            select(Product).where(Product.id == item.product_id).with_for_update()
        )
        product = result.scalar_one_or_none()

        if not product:
            order.status = "payment_failed"
            await db.commit()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {item.product_id} not found",
            )

        if product.stock < item.quantity:
            order.status = "payment_failed"
            await db.commit()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{product.name} is out of stock",
            )

    for item in order_items:
        result = await db.execute(select(Product).where(Product.id == item.product_id))
        product = result.scalar_one()
        product.stock -= item.quantity

    order.payment_id = f"pay_{uuid4().hex}"
    order.status = "paid"
    await db.commit()
    await db.refresh(order)

    return {
        "order_id": order.id,
        "payment_id": order.payment_id,
        "status": order.status,
        "amount": order.total_amount,
    }
