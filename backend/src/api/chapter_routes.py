from fastapi import APIRouter, HTTPException
from typing import List
from src.models.api_models import GetChaptersResponse, GetChapterResponse, ChapterListItem
from src.services.chapter_service import ChapterService
import src.models.base_models as models

chapter_router = APIRouter()
chapter_service = ChapterService()


@chapter_router.get("/chapters", response_model=GetChaptersResponse)
async def get_chapters():
    """
    Retrieve a list of all textbook chapters.
    """
    try:
        chapters = await chapter_service.get_all_chapters()
        chapter_list = [
            ChapterListItem(
                id=chapter.id,
                title=chapter.title,
                chapter_number=chapter.chapter_number,
                slug=chapter.slug,
                description=chapter.content[:100] + "..." if len(chapter.content) > 100 else chapter.content
            )
            for chapter in chapters
        ]
        return GetChaptersResponse(chapters=chapter_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving chapters: {str(e)}")


@chapter_router.get("/chapters/{chapter_id}", response_model=GetChapterResponse)
async def get_chapter(chapter_id: str):
    """
    Retrieve the content of a specific textbook chapter.
    """
    try:
        chapter = await chapter_service.get_chapter_by_id(chapter_id)
        if not chapter:
            raise HTTPException(status_code=404, detail="Chapter not found")
        
        return GetChapterResponse(
            id=chapter.id,
            title=chapter.title,
            chapter_number=chapter.chapter_number,
            slug=chapter.slug,
            content=chapter.content,
            created_at=chapter.created_at,
            updated_at=chapter.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving chapter: {str(e)}")