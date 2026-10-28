from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import APP_NAME, APP_VERSION
from app.database import Base, engine

import app.models

from app.routers.auth import router as auth_router
from app.routers.trips import router as trips_router
from app.routers.ai import router as ai_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="AI Travel Planner API",
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# Templates
templates = Jinja2Templates(directory="app/templates")

# Routers
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(
    trips_router,
    prefix="/trips",
    tags=["Trips"],
)

app.include_router(
    ai_router,
    prefix="/ai",
    tags=["AI"],
)


# Home Route (Temporary)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={}
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )