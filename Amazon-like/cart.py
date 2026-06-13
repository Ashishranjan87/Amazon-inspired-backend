from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db.session import AsyncSessionLocal
from models.cart import Cart_Model, Cart
from models.order import Order, OrderItem
from models.product import Product
from schemas.cart import AddToCart
from services.cart_service import add_to_cart, update_cart_items, remove_cart_items
from core.dependency import get_current_user
from models.user import User

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db




@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add(items: AddToCart, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await add_to_cart(db,current_user.id,items.product_id,items.quantity)


@router.post("/checkout", status_code=status.HTTP_200_OK)
async def checkout(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    try:
        result = await db.execute(
            select(Cart_Model).join(Cart).where(Cart.user_id == current_user.id)
        )
        cart_items = result.scalars().all()

        if not cart_items:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cart is empty"
            )

        total = 0
        order_items_data = []

        for item in cart_items:
            result = await db.execute(
                select(Product).where(Product.id == item.product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                raise HTTPException(status_code=404, detail="Product not found")

            if product.stock < item.quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"{product.name} is out of stock"
                )

            total += product.price * item.quantity

            order_items_data.append({
                "product": product,
                "quantity": item.quantity
            })

        order = Order(user_id=current_user.id, total_amount=total, status="pending_payment")
        db.add(order)
        await db.flush()

        for data in order_items_data:
            product = data["product"]
            quantity = data["quantity"]

            db.add(OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=product.price
            ))

        await db.execute(
            delete(Cart_Model).where(
                Cart_Model.cart_id.in_([item.cart_id for item in cart_items])
            )
        )

        await db.commit()

        return {
            "order_id": order.id,
            "total": order.total_amount,
            "status": order.status,
            "message": "Order created. Complete payment to place the order."
        }

    except Exception as e:
        await db.rollback()
        raise e


@router.put("/update")
async def update_cart(product_id: int, quantity: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await update_cart_items(db,current_user.id,product_id,quantity)

@router.delete("/delete")
async def delete_cart(product_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await remove_cart_items(db,current_user.id,product_id)

@router.get("/")
async def view_cart(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Cart).where(Cart.user_id == current_user.id))
    cart = result.scalar_one_or_none()

    if not cart:
        return {
            "user_id": current_user.id,
            "items": [],
            "total_items": 0,
            "total_amount": 0
        }

    result = await db.execute(
        select(Cart_Model, Product).join(
            Product,
            Product.id == Cart_Model.product_id
        ).where(
            Cart_Model.cart_id == cart.id
        )
    )
    cart_items = result.all()

    items = []
    total_amount = 0

    for cart_item, product in cart_items:
        subtotal = product.price * cart_item.quantity
        total_amount += subtotal

        items.append({
            "cart_item_id": cart_item.id,
            "product_id": product.id,
            "product_name": product.name,
            "quantity": cart_item.quantity,
            "price": product.price,
            "subtotal": subtotal
        })

    return {
        "user_id": current_user.id,
        "items": items,
        "total_items": len(items),
        "total_amount": total_amount
    }
