from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import (
    hash_password,
    verify_password,
)


class AuthService:

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str,
    ):

        email = email.strip().lower()

        print("=" * 60)
        print("Searching Email:", repr(email))

        users = db.query(User).all()

        print("Total Users:", len(users))

        for user in users:
            print(
                f"ID={user.id} | EMAIL={repr(user.email)}"
            )

        found_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        print("Query Result:", found_user)
        print("=" * 60)

        return found_user

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate,
    ):

        user.email = user.email.strip().lower()

        existing_user = AuthService.get_user_by_email(
            db,
            user.email,
        )

        if existing_user:
            return None

        db_user = User(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(
                user.password
            ),
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str,
    ):

        email = email.strip().lower()

        print("\n")
        print("=" * 60)
        print("LOGIN REQUEST")
        print("Email:", repr(email))
        print("Password:", repr(password))

        user = AuthService.get_user_by_email(
            db,
            email,
        )

        if user is None:
            print("❌ User NOT Found")
            print("=" * 60)
            return None

        print("✅ User Found")
        print("Database Email:", user.email)
        print("Stored Hash:", user.hashed_password)

        password_ok = verify_password(
            password,
            user.hashed_password,
        )

        print("Password Match:", password_ok)
        print("=" * 60)

        if not password_ok:
            return None

        return user