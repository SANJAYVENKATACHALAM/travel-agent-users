from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.trip import (
    TripCreate,
    TripUpdate,
    TripResponse,
)
from app.services.trip_service import TripService

router = APIRouter()


@router.post(
    "/",
    response_model=TripResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TripService.create_trip(
        db,
        trip,
        current_user,
    )


@router.get(
    "/",
    response_model=List[TripResponse],
)
def get_all_trips(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TripService.get_all_trips(
        db,
        current_user,
    )


@router.get(
    "/{trip_id}",
    response_model=TripResponse,
)
def get_trip(
    trip_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    trip = TripService.get_trip_by_id(
        db,
        trip_id,
        current_user,
    )

    if trip is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    return trip


@router.put(
    "/{trip_id}",
    response_model=TripResponse,
)
def update_trip(
    trip_id: int,
    trip: TripUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    updated_trip = TripService.update_trip(
        db,
        trip_id,
        trip,
        current_user,
    )

    if updated_trip is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    return updated_trip


@router.delete(
    "/{trip_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_trip(
    trip_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    deleted = TripService.delete_trip(
        db,
        trip_id,
        current_user,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    return None