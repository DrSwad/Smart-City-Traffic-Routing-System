from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.traffic import Intersection


class TrafficService:
    def __init__(self, db: Session):
        self.db = db

    def get_intersections(self) -> List[Intersection]:
        return self.db.query(Intersection).all()

    def get_intersection(self, intersection_id: int) -> Optional[Intersection]:
        return (
            self.db.query(Intersection)
            .filter(Intersection.id == intersection_id)
            .first()
        )

    def create_intersection(
        self, name: str, latitude: float, longitude: float, description: str = None
    ) -> Intersection:
        intersection = Intersection(
            name=name, latitude=latitude, longitude=longitude, description=description
        )
        self.db.add(intersection)
        self.db.commit()
        self.db.refresh(intersection)
        return intersection
