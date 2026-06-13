from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from db.session import AsyncSessionLocal
from models.order import Order
from schemas.payment import PaymentRequest, PaymentResponse
from services.payment_service import process_payment
from core.dependency import get_current_user
from models.user import User


router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


@router.post("/pay", status_code=status.HTTP_200_OK, response_model=PaymentResponse)
async def pay(payment: PaymentRequest, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await process_payment(db, payment,current_user.id)


@router.get("/{order_id}/status")
async def payment_status(order_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(
            Order.id == order_id,
            Order.user_id == current_user.id,
        )
    )
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return {
        "order_id": order.id,
        "status": order.status,
        "payment_id": order.payment_id,
        "amount": order.total_amount,
    }
