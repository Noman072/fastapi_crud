from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from schemas.item import Item, ItemCreate
from schemas.user import User
from services import item as item_service
from api.deps import get_current_user, get_current_admin_user
from database import get_db

router = APIRouter()

@router.get("/", response_model=List[Item])
async def read_items(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
):
    return await item_service.get_items(db, skip=skip, limit=limit)

@router.post("/", response_model=Item)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await item_service.create_item(db=db, item=item)

@router.delete("/{item_id}", response_model=Item)
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin_user),
):
    db_item = await item_service.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
