import asyncio
from typing import List, Optional
from datetime import datetime
from src.models.base_models import TextbookChapter, ChapterStatus
from src.utils.logger import logger


class ChapterService:
    """
    Service class for managing textbook chapters.
    In a real implementation, this would connect to a database.
    For this MVP, we'll use an in-memory store.
    """
    
    def __init__(self):
        # In-memory store for chapters (in production, this would be a database)
        self.chapters: List[TextbookChapter] = []
        self._load_sample_chapters()
    
    def _load_sample_chapters(self):
        """Load sample chapters for the textbook"""
        sample_titles = [
            "Introduction to Physical AI",
            "Basics of Humanoid Robotics", 
            "ROS 2 Fundamentals",
            "Digital Twin Simulation (Gazebo + Isaac)",
            "Vision-Language-Action Systems",
            "Capstone: Simple AI-Robot Pipeline"
        ]
        
        for i, title in enumerate(sample_titles, 1):
            chapter = TextbookChapter(
                id=f"chapter_{i}",
                title=title,
                content=f"Content for {title} goes here. This would include detailed explanations, code examples, and exercises.",
                chapter_number=i,
                slug=title.lower().replace(" ", "-").replace("(", "").replace(")", ""),
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=ChapterStatus.PUBLISHED
            )
            self.chapters.append(chapter)
    
    async def get_all_chapters(self) -> List[TextbookChapter]:
        """Get all published textbook chapters"""
        try:
            logger.log_info("Retrieving all chapters", operation="get_all_chapters")
            return [chapter for chapter in self.chapters if chapter.status == ChapterStatus.PUBLISHED]
        except Exception as e:
            logger.log_error("Error retrieving all chapters", error=e)
            raise
    
    async def get_chapter_by_id(self, chapter_id: str) -> Optional[TextbookChapter]:
        """Get a specific textbook chapter by its ID"""
        try:
            logger.log_info(f"Retrieving chapter with ID: {chapter_id}", operation="get_chapter_by_id")
            for chapter in self.chapters:
                if chapter.id == chapter_id and chapter.status != ChapterStatus.ARCHIVED:
                    return chapter
            return None
        except Exception as e:
            logger.log_error(f"Error retrieving chapter with ID: {chapter_id}", error=e)
            raise