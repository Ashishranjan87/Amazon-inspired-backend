from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db.session import AsyncSessionLocal
from models.product import Category, Product
from models.user import User
from schemas.product import ProductCreate
from schemas.response import ProductResponse
from services.product_service import create_product, get_product
from core.dependency import require_admin
from utils.cache import get_cache, set_cache, delete_cache
from core.limiter import limiter



router = APIRouter()
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@router.post("/categories")
async def create_category(name: str, db: AsyncSession = Depends(get_db), admin: User=Depends(require_admin)):
    category = Category(name=name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    await delete_cache("categories:all")
    return category


@router.get("/categories")
async def get_categories(request: Request,db: AsyncSession = Depends(get_db)):
    cache_key = f"categories:all"
    cached_categories = await get_cache(cache_key)
    if cached_categories is not None:
        return cached_categories
    result = await db.execute(select(Category).order_by(Category.name))
    categories = result.scalars().all()
    response = [
        {
            "id": category.id,
            "name": category.name,
        }
        for category in categories
    ]
    await set_cache(cache_key, response, expire_seconds=60*60*2)
    return response


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductCreate, db: AsyncSession = Depends(get_db),admin: User=Depends(require_admin)):
    return await create_product(db, product)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProductResponse])
@limiter.limit("10000/minute")
async def get_all_products(request: Request, search:str=None, min_price: int=None, max_price: int=None,
                           skip: int=0, limit: int=10,db: AsyncSession = Depends(get_db)):
    return await get_product(db, skip=skip, limit=limit, name=search, min_price=min_price, max_price=max_price)


@router.get("/{product_id}")
@limiter.limit("10000/minute")
async def get_product_by_id(request: Request, product_id: int, db: AsyncSession = Depends(get_db)):
    cache_key = f"products:details:{product_id}"
    cached_product = await get_cache(cache_key)
    if cached_product is not None:
        return cached_product
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    response = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "category_id": product.category_id,
    }
    await set_cache(cache_key, response, expire_seconds=60*60*2)
    return response


@router.put("/{product_id}/add-stock")
async def add_stock(product_id: int, quantity: int, db: AsyncSession = Depends(get_db),admin: User=Depends(require_admin)):

    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")

    product.stock += quantity

    await db.commit()
    await db.refresh(product)
    await delete_cache("products:all")
    await delete_cache(f"products:details:{product_id}")

    return {
        "message": "Stock increased",
        "new_stock": product.stock
    }
