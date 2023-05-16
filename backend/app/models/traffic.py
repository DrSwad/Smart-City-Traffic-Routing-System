from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.core.database import Base


class Intersection(Base):
    __tablename__ = "intersections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
