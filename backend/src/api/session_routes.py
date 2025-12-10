from fastapi import APIRouter, HTTPException
from src.models.api_models import CreateSessionRequest, CreateSessionResponse
from src.services.session_service import SessionService

session_router = APIRouter()
session_service = SessionService()


@session_router.post("/create", response_model=CreateSessionResponse)
async def create_session(request: CreateSessionRequest):
    """
    Create a new user session.
    """
    try:
        session = await session_service.create_session(
            user_agent=request.user_agent,
            additional_context=request.additional_context
        )
        return session
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating session: {str(e)}")