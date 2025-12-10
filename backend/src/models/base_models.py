from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class ChapterStatus(str, Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    ARCHIVED = "ARCHIVED"


class TextbookChapter(BaseModel):
    id: str
    title: str
    content: str
    chapter_number: int
    slug: str
    created_at: datetime
    updated_at: datetime
    status: ChapterStatus


class QueryType(str, Enum):
    GENERAL = "GENERAL"
    SELECTED_TEXT = "SELECTED_TEXT"
    NAVIGATION = "NAVIGATION"


class UserQuery(BaseModel):
    id: str
    query_text: str
    response_text: str
    source_chapters: list[str]  # list of chapter IDs that contributed to the response
    timestamp: datetime
    session_id: str
    query_type: QueryType


class RAGChatbot(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime


class ServiceType(str, Enum):
    QDRANT = "QDRANT"
    NEON = "NEON"
    FASTAPI = "FASTAPI"
    LLM_API = "LLM_API"


class ExternalService(BaseModel):
    id: str
    service_type: ServiceType
    service_name: str
    endpoint_url: str
    api_key: Optional[str] = None  # Should be stored securely in practice
    config_params: dict
    created_at: datetime
    updated_at: datetime


class UserSession(BaseModel):
    id: str
    start_time: datetime
    last_activity: datetime
    user_agent: Optional[str] = None
    ip_address: Optional[str] = None  # For analytics, not personal identification