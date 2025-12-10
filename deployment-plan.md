# Production Deployment Guide: Physical AI & Humanoid Robotics Textbook

## Overview

This document outlines the steps required to deploy the Physical AI & Humanoid Robotics textbook application to production. The application consists of:
- Frontend: Docusaurus-based textbook website deployed to GitHub Pages
- Backend: FastAPI application with RAG functionality deployed to Railway/Render
- External Services: Qdrant (vector database), Neon (PostgreSQL), OpenAI API

## Pre-deployment Checklist

- [ ] All development tasks completed and tested locally
- [ ] Repository ready on GitHub
- [ ] API keys for external services obtained
- [ ] Domain names (if applicable) registered and configured
- [ ] SSL certificates (if applicable) obtained
- [ ] Security audit completed
- [ ] Performance testing completed

## Backend Deployment (Railway/Render)

### Railway Deployment Steps

1. **Prepare for Railway Deployment**
   - Create a `Dockerfile` in the backend directory:
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY pyproject.toml poetry.lock ./
   
   RUN pip install poetry && poetry export -o requirements.txt -f requirements.txt --without-hashes
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8000
   
   CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Deploy to Railway**
   - Install Railway CLI: `npm install -g @railway/cli`
   - Login: `railway login`
   - Create new project: `railway init`
   - Set working directory to backend folder
   - Link to project: `railway link`
   - Set environment variables:
     ```
     railway vars set QDRANT_URL="your-qdrant-url"
     railway vars set QDRANT_API_KEY="your-qdrant-api-key"
     railway vars set NEON_DATABASE_URL="your-neon-database-url"
     railway vars set OPENAI_API_KEY="your-openai-api-key"
     railway vars set LLM_MODEL_NAME="gpt-3.5-turbo"
     railway vars set EMBEDDING_MODEL_NAME="text-embedding-ada-002"
     ```
   - Deploy: `railway up`

3. **Configure Database Connections**
   - Ensure Neon database is properly configured
   - Verify Qdrant collection exists for textbook embeddings
   - Test database connectivity

### Render Deployment Steps (Alternative)

1. **Prepare for Render Deployment**
   - Create a `Dockerfile` in the backend directory (same as Railway)
   - Create Render deployment configuration

2. **Deploy to Render**
   - Create new Web Service on Render
   - Connect to GitHub repository
   - Set root directory to: `backend`
   - Set Dockerfile path: `Dockerfile`
   - Set environment variables in Render dashboard:
     - QDRANT_URL
     - QDRANT_API_KEY
     - NEON_DATABASE_URL
     - OPENAI_API_KEY
     - LLM_MODEL_NAME
     - EMBEDDING_MODEL_NAME
   - Configure health check URL: `/`

## Frontend Deployment (GitHub Pages)

### Step 1: Build the Docusaurus Site

1. Navigate to the frontend directory:
   ```bash
   cd frontend/textbook-website
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the static site:
   ```bash
   npm run build
   ```

### Step 2: GitHub Pages Configuration

1. Create a GitHub Actions workflow file: `.github/workflows/deploy.yml`
   ```yaml
   name: Deploy to GitHub Pages

   on:
     push:
       branches: [ main ]
     workflow_dispatch:

   jobs:
     deploy:
       name: Deploy to GitHub Pages
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - uses: actions/setup-node@v3
           with:
             node-version: 18.x
             cache: npm
             cache-dependency-path: frontend/textbook-website/package-lock.json

         - name: Install dependencies
           run: |
             cd frontend/textbook-website
             npm ci

         - name: Build website
           run: |
             cd frontend/textbook-website
             npm run build

         # Popular action to deploy to GitHub Pages:
         # Docs: https://github.com/peaceiris/actions-gh-pages#%EF%B8%8F-docusaurus
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./frontend/textbook-website/build
             # The following lines assign commit authorship to the official
             # GH-Actions bot for deploys from the `main` branch:
             # https://github.com/actions/checkout/issues/13#issuecomment-724415212
             # If your site routinely has commits from multiple authors,
             # consider setting authorship to your personal GitHub account
             # or another specific user. See documentation for details.
             user_name: github-actions[bot]
             user_email: github-actions[bot]@users.noreply.github.com
   ```

2. Enable GitHub Pages in repository settings:
   - Go to repository Settings
   - Navigate to Pages section
   - Select source as "GitHub Actions"

3. Update `docusaurus.config.js` with the correct deployment URL:
   ```javascript
   module.exports = {
     // ...
     url: 'https://your-username.github.io', // Replace with your base URL
     baseUrl: '/your-repo-name/', // Replace with your repo name
     // ...
   };
   ```

### Step 3: Configure API Endpoint

Update the frontend to point to the production backend API in `src/components/ChatInterface.js`:
- Replace `http://localhost:8000` with the deployed backend URL

## Environment Variables

### Backend Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| QDRANT_URL | URL for Qdrant vector database | Yes |
| QDRANT_API_KEY | API key for Qdrant | Yes (if using cloud) |
| NEON_DATABASE_URL | Connection string for Neon PostgreSQL | Yes |
| OPENAI_API_KEY | API key for OpenAI services | Yes |
| LLM_MODEL_NAME | Name of the LLM to use (default: gpt-3.5-turbo) | No |
| EMBEDDING_MODEL_NAME | Name of the embedding model (default: text-embedding-ada-002) | No |

### Frontend Environment Variables (if needed)

| Variable | Description | Required |
|----------|-------------|----------|
| REACT_APP_BACKEND_API_URL | URL of the deployed backend API | Yes |

## Health Checks

### Backend Health Checks

1. **API Endpoint Health Check**: 
   - Endpoint: `GET /`
   - Expected response: 200 with welcome message

2. **Database Connectivity Check**:
   - Endpoint: `GET /health/db`
   - Expected response: 200 with database status

3. **External Service Connectivity Check**:
   - Endpoint: `GET /health/external`
   - Expected response: 200 with external service statuses (Qdrant, OpenAI, etc.)

### Frontend Health Checks

1. **Page Load Testing**: Verify all textbook chapters load correctly
2. **Chat Functionality Test**: Test the RAG chatbot functionality
3. **Text Selection Feature**: Verify text selection and "Ask AI" functionality

## Post-Deployment Steps

1. **Verify All Functionality**:
   - Test navigation through all textbook chapters
   - Verify RAG chatbot responses are accurate and reference textbook content
   - Test text selection and ask functionality
   - Confirm all hyperlinks work correctly

2. **Performance Testing**:
   - Check page load speeds (especially important for GitHub Pages)
   - Verify RAG response times are under 5 seconds
   - Test concurrent user scenarios

3. **Security Verification**:
   - Confirm no sensitive information is exposed
   - Verify API rate limiting or authentication if necessary
   - Ensure proper error handling doesn't leak sensitive details

4. **Analytics Setup**:
   - Implement basic analytics for user engagement
   - Track which chapters are accessed most frequently
   - Monitor RAG usage patterns

## Rollback Plan

In case of critical issues post-deployment:

1. **Frontend Rollback**:
   - Use GitHub Pages to serve a previous stable build
   - Revert to a previous commit in the repository

2. **Backend Rollback**:
   - For Railway: Use the Railway dashboard to revert to a previous deployment
   - For Render: Revert to a previous release in the dashboard

## Monitoring and Maintenance

### Monitoring Setup

1. **Backend Monitoring**:
   - API response times
   - Error rates
   - Database connection health
   - External API usage

2. **Frontend Monitoring**:
   - Page load times
   - User engagement metrics
   - Error tracking

### Maintenance Schedule

- Weekly: Review logs and error reports
- Monthly: Update dependencies in backend and frontend
- Quarterly: Review API usage costs and optimize if needed
- As needed: Update textbook content and refresh embeddings

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **Rate Limiting**: Consider implementing rate limiting for free-tier usage
3. **Input Validation**: Ensure all user inputs are properly validated
4. **Data Privacy**: No personal user data is stored (as per requirements)
5. **SSL/TLS**: Ensure all connections use HTTPS

## Cost Optimization for Free Tier

1. **Monitor Usage**: Regularly check usage of Neon, Qdrant, and OpenAI APIs
2. **Implement Caching**: Add caching for frequently requested data
3. **Optimize Embeddings**: Use cost-effective embedding models where possible
4. **Session Management**: Limit session duration to reduce resource usage