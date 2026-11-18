from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, func
from .database import Base


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(100), nullable=False)
    crude_fiber = Column(Numeric(5, 2), nullable=False)
    fat_ratio = Column(Numeric(5, 2), nullable=False)
    gas_label = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())