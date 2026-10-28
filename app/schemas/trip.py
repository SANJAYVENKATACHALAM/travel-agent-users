from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TripCreate(BaseModel):
    title: str
    destination: str
    start_date: date
    end_date: date
    budget: float
    travelers: int
    transport: Optional[str] = None
    accommodation: Optional[str] = None
    preferences: Optional[str] = None


class TripUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[float] = None
    travelers: Optional[int] = None
    transport: Optional[str] = None
    accommodation: Optional[str] = None
    preferences: Optional[str] = None
    status: Optional[str] = None
    itinerary: Optional[str] = None


class TripResponse(BaseModel):
    id: int
    title: str
    destination: str
    start_date: date
    end_date: date
    budget: float
    travelers: int
    transport: Optional[str]
    accommodation: Optional[str]
    preferences: Optional[str]
    status: str
    itinerary: Optional[str]
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)