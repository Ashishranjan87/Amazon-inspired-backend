from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from models.cart import Cart, Cart_Model


async def add_to_cart(db, user_id, product_id, quantity):
    result = await db.execute(select(Cart).where(Cart.user_id == user_id))
    cart = result.scalar_one_or_none()

    if cart is None:
        cart = Cart(user_id= user_id)
        db.add(cart)
        await db.commit()
        await db.refresh(cart)

    result = await db.execute(
        select(Cart_Model).where(
            Cart_Model.cart_id == cart.id,
            Cart_Model.product_id == product_id,
        )
    )
    items = result.scalar_one_or_none()

    if items:
        items.quantity = items.quantity + quantity
    else:
        items = Cart_Model(
            cart_id = cart.id,
            product_id = product_id,
            quantity = quantity
        )
        db.add(items)

    await db.commit()
    return {"message": "Added to cart"}

async def update_cart_items(db, user_id, product_id, quantity):
    result = await db.execute(select(Cart).where(Cart.user_id == user_id))
    cart = result.scalar_one_or_none()

    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart not found",
        )

    result = await db.execute(
        select(Cart_Model).where(
            Cart_Model.cart_id == cart.id,
            Cart_Model.product_id == product_id,
        )
    )
    items = result.scalar_one_or_none()

    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    items.quantity = quantity
    await db.commit()

    return {"message": "Updated"}

async def remove_cart_items(db, user_id, product_id):
    result = await db.execute(select(Cart).where(Cart.user_id == user_id))
    cart = result.scalar_one_or_none()

    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart not found",
        )

    result = await db.execute(
        select(Cart_Model).where(
            Cart_Model.cart_id == cart.id,
            Cart_Model.product_id == product_id,
        )
    )
    items = result.scalar_one_or_none()

    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    await db.delete(items)
    await db.commit()

    return {"message": "Removed"}
