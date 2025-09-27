from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
