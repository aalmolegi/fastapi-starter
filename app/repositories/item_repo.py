from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.item import Item

def create(db: Session, owner_id: int, title: str, description: str | None) -> Item:
    item = Item(owner_id=owner_id, title=title, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get(db: Session, item_id: int) -> Item | None:
    return db.get(Item, item_id)

def list_for_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 50) -> list[Item]:
    stmt = select(Item).where(Item.owner_id == owner_id).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())

def update(db: Session, item: Item, title: str | None, description: str | None) -> Item:
    if title is not None:
        item.title = title
    if description is not None:
        item.description = description
    db.commit()
    db.refresh(item)
    return item

def delete(db: Session, item: Item) -> None:
    db.delete(item)
    db.commit()
