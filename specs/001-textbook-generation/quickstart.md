# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-textbook-generation
**Date**: 2025-12-10

## Overview

This guide will help you quickly set up and run the Physical AI & Humanoid Robotics textbook with integrated RAG chatbot. The system consists of a Docusaurus frontend for the textbook content and a FastAPI backend for the RAG functionality.

## Prerequisites

- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for FastAPI backend)
- Poetry (for Python dependency management) or pip
- Access to Qdrant vector database (can be local or cloud)
- Access to Neon PostgreSQL database (can be local or cloud)
- LLM API key (OpenAI or equivalent)

## Setup

### 1. Backend Setup (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the backend server:
   ```bash
   poetry run uvicorn src.api.main:app --reload
   ```

### 2. Frontend Setup (Docusaurus)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your backend API URL
   ```

4. Run the development server:
   ```bash
   npm run start
   ```

## Configuration

### Database Setup

1. Set up Neon database and get connection URL
2. Set up Qdrant instance and get API key/URL
3. Update your `.env` files accordingly

### LLM Configuration

1. Obtain an API key from your preferred LLM provider (OpenAI, Anthropic, etc.)
2. Update the `LLM_API_KEY` in your backend `.env` file
3. Configure the appropriate LLM settings in the service configuration

### Textbook Content

1. Add your textbook content to the `frontend/content` directory
2. Follow the existing chapter structure (chapters 1-6)
3. Content should be in Markdown format with appropriate metadata

## Running in Development

### Local Development

1. Start the backend server: `poetry run uvicorn src.api.main:app --reload`
2. In a separate terminal, start the frontend: `npm run start`
3. Access the textbook at `http://localhost:3000`
4. The API will be available at `http://localhost:8000`

### Testing

1. Run backend tests: `poetry run pytest`
2. Run frontend tests: `npm run test`

## Deployment

### GitHub Pages (Frontend)

1. Build the frontend: `npm run build`
2. The output will be in the `build` directory
3. Configure GitHub Pages to serve from this directory

### Backend Deployment

1. The backend can be deployed to any platform that supports Python/ASGI (e.g., Render, Railway)
2. Ensure environment variables are configured appropriately
3. Run the production server: `uvicorn src.api.main:app`

## Troubleshooting

### Common Issues

1. **Build times exceed 2 minutes**: 
   - Check for large images or assets that can be optimized
   - Review Docusaurus configuration for performance settings

2. **RAG responses are slow**:
   - Ensure Qdrant is properly configured and accessible
   - Check LLM API response times

3. **Free-tier limits exceeded**:
   - Monitor API usage for your LLM and vector database
   - Implement caching if needed