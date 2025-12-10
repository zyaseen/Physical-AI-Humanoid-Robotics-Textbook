from fastapi import APIRouter, HTTPException
from src.models.api_models import (
    ChatbotQueryRequest, 
    ChatbotQueryResponse, 
    QueryWithSelectionRequest, 
    QueryWithSelectionResponse
)
from src.services.query_service import QueryService

chatbot_router = APIRouter()
query_service = QueryService()


@chatbot_router.post("/query", response_model=ChatbotQueryResponse)
async def chatbot_query(request: ChatbotQueryRequest):
    """
    Submit a query to the RAG chatbot and receive a response based on textbook content.
    """
    try:
        result = await query_service.process_general_query(
            query_text=request.query,
            context=request.context,
            options=request.options
        )
        return result
    except ValueError as e:
        if "length" in str(e).lower():
            raise HTTPException(status_code=400, detail={
                "error": str(e),
                "code": "INVALID_QUERY_LENGTH"
            })
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error": "Error processing RAG query",
            "code": "RAG_PROCESSING_ERROR",
            "details": str(e)
        })


@chatbot_router.post("/query-with-selection", response_model=QueryWithSelectionResponse)
async def chatbot_query_with_selection(request: QueryWithSelectionRequest):
    """
    Submit a query based on selected text in the textbook.
    """
    try:
        result = await query_service.process_selection_query(
            selected_text=request.selected_text,
            additional_context=request.additional_context,
            session_id=request.session_id
        )
        return result
    except ValueError as e:
        if "length" in str(e).lower():
            raise HTTPException(status_code=400, detail={
                "error": str(e),
                "code": "INVALID_QUERY_LENGTH"
            })
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error": "Error processing selection query",
            "code": "RAG_PROCESSING_ERROR",
            "details": str(e)
        })