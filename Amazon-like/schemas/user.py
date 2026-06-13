from datetime import date

from typing import Literal, Annotated
from pydantic import BaseModel, EmailStr, field_validator, Field


class userCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not any(c.isupper() for c in value):
            raise ValueError("Password must contain an uppercase letter")

        if not any(c.islower() for c in value):
            raise ValueError("Password must contain a lowercase letter")

        if not any(c.isdigit() for c in value):
            raise ValueError("Password must contain a digit")

        return value

    # firstname: Annotated[
    #     str,
    #     Field(
    #         min_length=2,
    #         max_length=50,
    #         pattern=r"^[A-Za-z]+$"
    #     )
    # ]
    #
    # lastname: Annotated[
    #     str,
    #     Field(
    #         min_length=2,
    #         max_length=50,
    #         pattern=r"^[A-Za-z]+$"
    #     )
    # ]

    role: Literal["admin", "user"] = "user"

    date_of_birth: date

class userLogin(BaseModel):
    email: EmailStr
    password: str
    role: Literal["admin", "user"] = "user"
    id: Annotated[int, ...]
