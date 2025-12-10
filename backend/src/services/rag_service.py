from typing import List, Tuple
from src.utils.logger import logger
from src.services.embedding_service import EmbeddingService
from src.services.llm_service import LLMService


class RAGService:
    """
    Service class for implementing RAG (Retrieval-Augmented Generation) functionality.
    This service connects to the vector database (Qdrant) and LLM API to generate
    answers based on textbook content.
    """

    def __init__(self):
        # In a real implementation, this would connect to Qdrant
        # For this MVP, we'll store embeddings in memory
        self.embeddings_store = {}  # chapter_id -> embedding
        self.content_store = {}     # chapter_id -> content

        # Services for actual implementation
        self.embedding_service = EmbeddingService()
        self.llm_service = LLMService()

        # Load textbook content (in memory for MVP)
        self._load_textbook_content()

    def _load_textbook_content(self):
        """
        Load textbook content for the RAG service.
        In a real implementation, this would pull from the database.
        """
        # For this MVP, we'll simulate with sample content
        sample_content = [
            ("chapter_1", "Introduction to Physical AI covers fundamental concepts in artificial intelligence applied to physical systems. This includes perception, planning, control, and learning in embodied agents."),
            ("chapter_2", "Basics of Humanoid Robotics include understanding the structure and mechanics of bipedal robots. Topics include kinematics, dynamics, balance control, and gait generation."),
            ("chapter_3", "ROS 2 Fundamentals covers the Robot Operating System concepts including nodes, topics, services, actions, and packages. Essential for robotic development."),
            ("chapter_4", "Digital Twin Simulation using Gazebo and Isaac Sim provides virtual environments for testing robotic algorithms before real-world deployment."),
            ("chapter_5", "Vision-Language-Action Systems integrates perception, language understanding, and action planning for intelligent robot behavior."),
            ("chapter_6", "Capstone: Simple AI-Robot Pipeline demonstrates integrating all concepts learned into a complete robotic system.")
        ]

        for chapter_id, content in sample_content:
            self.content_store[chapter_id] = content

    async def get_answer_from_textbook(self, query: str) -> Tuple[str, List[str]]:
        """
        Retrieve relevant content from textbook and generate an answer using LLM.
        Returns a tuple of (answer_text, source_chapter_ids)
        """
        try:
            # In a real implementation, this would:
            # 1. Create embeddings for the query
            query_embedding = await self.embedding_service.get_embedding(query)

            # 2. Search Qdrant vector database for relevant textbook content
            # For this MVP, we'll do a simple similarity search
            relevant_chapters = await self._find_relevant_chapters(query_embedding, top_k=2)

            # 3. Retrieve content for relevant chapters
            relevant_contents = [self.content_store[chapter_id] for chapter_id in relevant_chapters if chapter_id in self.content_store]

            # 4. Use LLM to generate a response based on retrieved content
            response = await self.llm_service.generate_response_with_context(query, relevant_contents)

            logger.log_info(f"Generated RAG response for query: {query[:30]}...", operation="get_answer_from_textbook")

            return response, relevant_chapters
        except Exception as e:
            logger.log_error("Error generating RAG response", error=e)
            raise

    async def _find_relevant_chapters(self, query_embedding: List[float], top_k: int = 2) -> List[str]:
        """
        Find the most relevant chapters based on embedding similarity.
        In a real implementation, this would query the vector database (Qdrant).
        """
        # For this MVP, we'll do a simple similarity search
        similarities = []

        for chapter_id, content in self.content_store.items():
            # Create embedding for the content
            content_embedding = await self.embedding_service.get_embedding(content)

            # Calculate cosine similarity (simplified)
            similarity = self._cosine_similarity(query_embedding, content_embedding)
            similarities.append((chapter_id, similarity))

        # Sort by similarity and return top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [chapter_id for chapter_id, _ in similarities[:top_k]]

    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculate cosine similarity between two vectors.
        This is a simplified implementation for the MVP.
        """
        # For the MVP, we'll use a simplified similarity calculation
        # In a real implementation, proper cosine similarity would be calculated
        min_len = min(len(vec1), len(vec2))
        dot_product = sum(vec1[i] * vec2[i] for i in range(min_len))
        magnitude1 = sum(x*x for x in vec1[:min_len]) ** 0.5
        magnitude2 = sum(x*x for x in vec2[:min_len]) ** 0.5

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)

    async def add_textbook_content(self, chapter_id: str, content: str):
        """
        Add textbook content to the vector database for RAG retrieval.
        In a real implementation, this would generate embeddings and store in Qdrant.
        """
        try:
            # Generate embedding for the content
            embedding = await self.embedding_service.get_embedding(content)

            # Store in memory (in real implementation, store in Qdrant)
            self.embeddings_store[chapter_id] = embedding
            self.content_store[chapter_id] = content

            logger.log_info(f"Added textbook content for chapter: {chapter_id}", operation="add_textbook_content")
        except Exception as e:
            logger.log_error(f"Error adding textbook content for chapter: {chapter_id}", error=e)
            raise