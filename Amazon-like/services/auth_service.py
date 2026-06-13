from fastapi import HTTPException
from sqlalchemy import select

from core.security import hash_password, verify_password, create_access_token

from datetime import datetime, date
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

async def register_user(db: AsyncSession, email: str, password: str, date_of_birth: date, role: str):
    user = User(
        email=email,
        password=hash_password(password),
        date_of_birth = date_of_birth,
        role = role,
        # system-managed fields
        is_active=True,
        created_at=datetime.now(),

        # forgot password fields (initially empty)
        reset_token=None,
        reset_token_expiry=None
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.password):
        return None
    return user

async def login_user(db: AsyncSession, email: str, password: str):
    user = await authenticate_user(db, email, password)
    if not user:
        return None
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    token = create_access_token({
    "sub": user.email,
    "user_id": user.id,
    "role": user.role
    })
    return token
