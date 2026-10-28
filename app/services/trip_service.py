from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.models.user import User
from app.schemas.trip import (
    TripCreate,
    TripUpdate,
)


class TripService:

    @staticmethod
    def create_trip(
        db: Session,
        trip: TripCreate,
        current_user: User,
    ):

        db_trip = Trip(
            title=trip.title,
            destination=trip.destination,
            start_date=trip.start_date,
            end_date=trip.end_date,
            budget=trip.budget,
            travelers=trip.travelers,
            transport=trip.transport,
            accommodation=trip.accommodation,
            preferences=trip.preferences,
            user_id=current_user.id,
        )

        db.add(db_trip)
        db.commit()
        db.refresh(db_trip)

        return db_trip

    @staticmethod
    def get_all_trips(
        db: Session,
        current_user: User,
    ):

        return (
            db.query(Trip)
            .filter(Trip.user_id == current_user.id)
            .order_by(Trip.created_at.desc())
            .all()
        )

    @staticmethod
    def get_trip_by_id(
        db: Session,
        trip_id: int,
        current_user: User,
    ):

        return (
            db.query(Trip)
            .filter(
                Trip.id == trip_id,
                Trip.user_id == current_user.id,
            )
            .first()
        )

    @staticmethod
    def update_trip(
        db: Session,
        trip_id: int,
        trip_data: TripUpdate,
        current_user: User,
    ):

        trip = TripService.get_trip_by_id(
            db,
            trip_id,
            current_user,
        )

        if trip is None:
            return None

        update_data = trip_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(trip, key, value)

        db.commit()
        db.refresh(trip)

        return trip

    @staticmethod
    def delete_trip(
        db: Session,
        trip_id: int,
        current_user: User,
    ):

        trip = TripService.get_trip_by_id(
            db,
            trip_id,
            current_user,
        )

        if trip is None:
            return False

        db.delete(trip)
        db.commit()

        return True