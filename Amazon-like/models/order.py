from sqlalchemy import Integer, ForeignKey, Column, Float, String
from db.session import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    total_amount = Column(Float)
    status = Column(String, default="pending")
    payment_id = Column(String, nullable=True)


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer)
    price = Column(Float)
