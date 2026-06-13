from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from schemas.user import userCreate, userLogin
from services.auth_service import register_user, login_user
from db.session import AsyncSessionLocal
from core.limiter import limiter

router = APIRouter()
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


@router.post("/signup")
@limiter.limit("10/minute")
async def signup(request: Request, user: userCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalar_one_or_none()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await register_user(db, user.email, user.password, user.date_of_birth, user.role)

@router.post("/login")
@limiter.limit("20/minute")
async def login(request: Request,user: userLogin, db: AsyncSession = Depends(get_db)):
    token = await login_user(db, user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
            "access_token": token,
            "token_type": "bearer"
            }
