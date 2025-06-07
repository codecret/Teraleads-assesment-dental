from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints import chatbot, patients, dashboard, auth

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(patients.router, prefix="/api/v1/patients", tags=["patients"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["chatbot"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"]) 