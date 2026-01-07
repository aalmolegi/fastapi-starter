from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.schemas.item import ItemCreate, ItemOut, ItemUpdate
from app.repositories import item_repo

router = APIRouter(prefix="/items", tags=["items"])

@router.post("", response_model=ItemOut, status_code=201)
def create_item(
    payload: ItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return item_repo.create(db, owner_id=current_user.id, title=payload.title, description=payload.description)

@router.get("", response_model=list[ItemOut])
def list_items(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return item_repo.list_for_owner(db, owner_id=current_user.id, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=ItemOut)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    item = item_repo.get(db, item_id)
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.patch("/{item_id}", response_model=ItemOut)
def update_item(
    item_id: int,
    payload: ItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    item = item_repo.get(db, item_id)
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_repo.update(db, item, title=payload.title, description=payload.description)

@router.delete("/{item_id}", status_code=204)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    item = item_repo.get(db, item_id)
    if not item or item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    item_repo.delete(db, item)
    return None
