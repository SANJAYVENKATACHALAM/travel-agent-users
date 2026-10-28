from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User

from app.schemas.ai import (
    AITripRequest,
    AITripResponse,
)

from app.services.ai_service import AIService

router = APIRouter()

ai_service = AIService()


@router.post(
    "/generate",
    response_model=AITripResponse,
)
def generate_itinerary(
    request: AITripRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    itinerary = ai_service.generate_itinerary(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        travelers=request.travelers,
        interests=request.interests,
    )

    return AITripResponse(
        itinerary=itinerary
    )