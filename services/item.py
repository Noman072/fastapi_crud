from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate

async def get_items(db: Session, skip: int = 0, limit: int = 100):
    return await db.execute(Item.__table__.select().offset(skip).limit(limit)).all()

async def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def delete_item(db: Session, item_id: int):
    db_item = await db.get(Item, item_id)
    if db_item:
        await db.delete(db_item)
        await db.commit()
    return db_item
