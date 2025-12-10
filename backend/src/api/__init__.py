from fastapi import APIRouter
from . import chapter_routes, chatbot_routes, session_routes

# Main API router
api_router = APIRouter()

# Include all route routers
api_router.include_router(chapter_routes.chapter_router, prefix="/textbook", tags=["textbook"])
api_router.include_router(chatbot_routes.chatbot_router, prefix="/chatbot", tags=["chatbot"])
api_router.include_router(session_routes.session_router, prefix="/session", tags=["session"])