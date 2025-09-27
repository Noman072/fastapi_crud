from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import get_password_hash

async def get_user_by_email(db: Session, email: str):
    return await db.execute(User.__table__.select().where(User.email == email)).first()

async def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
