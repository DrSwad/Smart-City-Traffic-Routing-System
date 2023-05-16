from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class IntersectionBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    description: Optional[str] = None


class IntersectionCreate(IntersectionBase):
    pass


class Intersection(IntersectionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
