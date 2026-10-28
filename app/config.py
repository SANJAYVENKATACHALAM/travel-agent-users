import os

from dotenv import load_dotenv

load_dotenv()

# ==========================
# Application
# ==========================

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Travel Planner"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

# ==========================
# Database
# ==========================

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

# ==========================
# Authentication
# ==========================

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = os.getenv(
    "ALGORITHM"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60
    )
)

# ==========================
# AI
# ==========================

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)