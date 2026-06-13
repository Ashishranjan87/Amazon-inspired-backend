import cart
import product
import auth
import payment
import order
import health
from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler

from core.limiter import limiter

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.get("/")
async def root():
    return {"message": "Amazon backend running 🚀"}



app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(product.router, prefix="/product", tags=["Product"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])
app.include_router(order.router, prefix="/order", tags=["Order"])
app.include_router(health.router, prefix="/health", tags=["Health"])
