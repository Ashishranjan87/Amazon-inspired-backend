from sqlalchemy import select


from utils.cache import get_cache, set_cache, delete_cache
from models.product import Product


PRODUCTS_CACHE_KEY = "products:all"
PRODUCTS_CACHE_TTL = 60*60*2

async def create_product(db, data):
    product = Product(**data.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    await delete_cache(PRODUCTS_CACHE_KEY)
    return product

async def get_product(db, name=None, min_price=None, max_price=None, skip: int=0, limit:int=10):
    cached_products = await get_cache(PRODUCTS_CACHE_KEY)
    if cached_products is None:
        result = await db.execute(select(Product))
        products = result.scalars().all()
        cached_products = [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
            }
            for product in products
        ]
        await set_cache(PRODUCTS_CACHE_KEY, cached_products, expire_seconds=PRODUCTS_CACHE_TTL)

    filtered_products = cached_products
    if name:
        search_text = name.lower()
        filtered_products = [
            product for product in filtered_products
            if search_text in product["name"].lower()
        ]

    if min_price is not None:
        filtered_products = [
            product for product in filtered_products
            if product["price"] >= min_price
        ]

    if max_price is not None:
        filtered_products = [
            product for product in filtered_products
            if product["price"] <= max_price
        ]

    return filtered_products[skip: skip + limit]

