from pydantic import BaseModel

class ItemCreate(BaseModel):
    title: str
    description: str | None = None

class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class ItemOut(BaseModel):
    id: int
    title: str
    description: str | None
    owner_id: int

    model_config = {"from_attributes": True}
