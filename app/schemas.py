from datetime import datetime
from pydantic import BaseModel, ConfigDict


class FoodBase(BaseModel):
    food_name: str
    crude_fiber: float
    fat_ratio: float
    gas_label: bool = False


class FoodCreate(FoodBase):
    pass


class FoodResponse(FoodBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None