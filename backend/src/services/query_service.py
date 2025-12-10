import uuid
from datetime import datetime
from typing import List, Optional
from src.models.api_models import (
    ChatbotQueryResponse, 
    QueryWithSelectionResponse, 
    SourceReference
)
from src.models.base_models import UserQuery, QueryType
from src.services.chapter_service import ChapterService
from src.services.rag_service import RAGService
from src.utils.logger import logger


class QueryService:
    """
    Service class for handling user queries to the RAG chatbot.
    """
    
    def __init__(self):
        self.chapter_service = ChapterService()
        self.rag_service = RAGService()
    
    async def process_general_query(
        self, 
        query_text: str, 
        context: dict = None, 
        options: dict = None
    ) -> ChatbotQueryResponse:
        """Process a general query from the user"""
        try:
            # Validate query length
            if len(query_text) < 5 or len(query_text) > 500:
                raise ValueError("Query must be between 5 and 500 characters")
            
            # Use RAG service to generate response
            response_text, source_chapters = await self.rag_service.get_answer_from_textbook(query_text)
            
            # Create source references
            source_refs = []
            if source_chapters:
                for chapter_id in source_chapters:
                    chapter = await self.chapter_service.get_chapter_by_id(chapter_id)
                    if chapter:
                        source_refs.append(
                            SourceReference(
                                chapter_id=chapter.id,
                                chapter_title=chapter.title,
                                relevance=0.9  # Default relevance, in real implementation this would come from RAG
                            )
                        )
            
            # Create response
            response = ChatbotQueryResponse(
                id=str(uuid.uuid4()),
                query=query_text,
                response=response_text,
                sources=source_refs,
                timestamp=datetime.now(),
                session_id=context.get("sessionId", "unknown") if context else "unknown"
            )
            
            logger.log_info(f"Processed general query with ID: {response.id}", operation="process_general_query")
            
            return response
        except Exception as e:
            logger.log_error("Error processing general query", error=e)
            raise
    
    async def process_selection_query(
        self,
        selected_text: str,
        additional_context: str = None,
        session_id: str = None
    ) -> QueryWithSelectionResponse:
        """Process a query based on selected text"""
        try:
            # Validate selected text length
            if len(selected_text) < 5 or len(selected_text) > 2000:
                raise ValueError("Selected text must be between 5 and 2000 characters")
            
            # Combine selected text with additional context
            query_text = selected_text
            if additional_context:
                query_text = f"{selected_text}\n\nAdditional context: {additional_context}"
            
            # Use RAG service to generate response
            response_text, source_chapters = await self.rag_service.get_answer_from_textbook(query_text)
            
            # Create source references
            source_refs = []
            if source_chapters:
                for chapter_id in source_chapters:
                    chapter = await self.chapter_service.get_chapter_by_id(chapter_id)
                    if chapter:
                        source_refs.append(
                            SourceReference(
                                chapter_id=chapter.id,
                                chapter_title=chapter.title,
                                relevance=0.9  # Default relevance, in real implementation this would come from RAG
                            )
                        )
            
            # Create response
            response = QueryWithSelectionResponse(
                id=str(uuid.uuid4()),
                selected_text=selected_text,
                response=response_text,
                sources=source_refs,
                timestamp=datetime.now(),
                session_id=session_id or "unknown"
            )
            
            logger.log_info(f"Processed selection query with ID: {response.id}", operation="process_selection_query")
            
            return response
        except Exception as e:
            logger.log_error("Error processing selection query", error=e)
            raise