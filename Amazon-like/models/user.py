from datetime import datetime

from sqlalchemy import Integer, String, Column, DateTime, Boolean, Date
from db.session import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    date_of_birth = Column(Date, nullable=True)
    # firstname = Column(String)
    # lastname = Column(String)
    role = Column(String, nullable=False, default="user")
    is_active = Column(Boolean, default=True)

    # 🔑 Forgot password support
    reset_token = Column(String, nullable=True)
    reset_token_expiry = Column(DateTime, nullable=True)

    # 📅 Metadata
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
