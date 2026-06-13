from pydantic import BaseModel, Field


class PaymentRequest(BaseModel):
    order_id: int
    amount: float = Field(gt=0)
    payment_token: str = Field(min_length=3)


class PaymentResponse(BaseModel):
    order_id: int
    payment_id: str
    status: str
    amount: float
