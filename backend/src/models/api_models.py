from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from .base_models import TextbookChapter


class ChapterListItem(BaseModel):
    id: str
    title: str
    chapter_number: int
    slug: str
    description: Optional[str] = None


class GetChaptersResponse(BaseModel):
    chapters: List[ChapterListItem]


class GetChapterResponse(BaseModel):
    id: str
    title: str
    chapter_number: int
    slug: str
    content: str
    created_at: datetime
    updated_at: datetime


class SourceReference(BaseModel):
    chapter_id: str
    chapter_title: str
    relevance: float  # Relevance score between 0 and 1


class ChatbotQueryRequest(BaseModel):
    query: str
    context: Optional[dict] = None
    options: Optional[dict] = None


class ChatbotQueryResponse(BaseModel):
    id: str
    query: str
    response: str
    sources: List[SourceReference]
    timestamp: datetime
    session_id: str


class QueryWithSelectionRequest(BaseModel):
    selected_text: str
    additional_context: Optional[str] = None
    session_id: str


class QueryWithSelectionResponse(BaseModel):
    id: str
    selected_text: str
    response: str
    sources: List[SourceReference]
    timestamp: datetime
    session_id: str


class CreateSessionRequest(BaseModel):
    user_agent: Optional[str] = None
    additional_context: Optional[dict] = None


class CreateSessionResponse(BaseModel):
    session_id: str
    timestamp: datetime