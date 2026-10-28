from pydantic import BaseModel
class AITripRequest(BaseModel):
    destination: str
    days: int
    budget: float
    travelers: int
    interests: str
class AITripResponse(BaseModel):
    itinerary: str