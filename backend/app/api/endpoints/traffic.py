from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.schemas import (
    Intersection,
    IntersectionCreate,
)
from app.services.traffic_service import TrafficService

router = APIRouter()


@router.get("/intersections", response_model=List[Intersection])
def get_intersections(db: Session = Depends(get_db)):
    service = TrafficService(db)
    return service.get_intersections()


@router.post("/intersections", response_model=Intersection)
def create_intersection(
    intersection: IntersectionCreate, db: Session = Depends(get_db)
):
    service = TrafficService(db)
    return service.create_intersection(
        name=intersection.name,
        latitude=intersection.latitude,
        longitude=intersection.longitude,
        description=intersection.description,
    )


@router.get("/intersections/{intersection_id}", response_model=Intersection)
def get_intersection(intersection_id: int, db: Session = Depends(get_db)):
    service = TrafficService(db)
    intersection = service.get_intersection(intersection_id)
    if not intersection:
        raise HTTPException(status_code=404, detail="Intersection not found")
    return intersection
