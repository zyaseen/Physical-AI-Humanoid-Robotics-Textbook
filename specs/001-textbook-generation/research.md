# Research Findings: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-textbook-generation
**Date**: 2025-12-10
**Researcher**: Qwen

## Research Tasks & Findings

### 1. Docusaurus Implementation Research

**Task**: Research Docusaurus implementation for textbook with 6 chapters

**Decision**: Use Docusaurus with custom styling for textbook content

**Rationale**: Docusaurus is ideal for documentation sites and can be customized for textbook-style content. It supports MDX (Markdown with React), has excellent navigation features, and can be deployed to GitHub Pages.

**Alternatives considered**:
- GitBook: More limited customization options
- VuePress: Would require learning Vue ecosystem
- Custom React app: More complex to implement and maintain

### 2. RAG Implementation Research

**Task**: Research RAG implementation using Qdrant, Neon, and FastAPI

**Decision**: Use LangChain with Qdrant vector store and FastAPI backend

**Rationale**: LangChain provides excellent integration with various LLMs and vector stores, making it ideal for RAG applications. Qdrant is efficient as a vector database and supports free-tier usage.

**Alternatives considered**:
- LlamaIndex: Another strong option but LangChain has broader community support
- Haystack: More complex setup with less clear free-tier support

### 3. LLM API Selection Research

**Task**: Research LLM API options that work with minimal GPU usage and free-tier constraints

**Decision**: Use OpenAI API with text-embedding-ada-002 for embeddings and gpt-3.5-turbo for responses, or consider open-source alternatives like Mistral via Hugging Face Inference API

**Rationale**: OpenAI provides reliable, high-quality responses and embeddings. Their pricing model works well for low-volume applications. Open-source alternatives via Hugging Face can reduce costs but may require more setup.

**Alternatives considered**:
- Anthropic Claude: Good quality but may be more expensive
- Hugging Face models: Cost-effective but may require more tuning

### 4. Text Selection Feature Research

**Task**: Research implementation of "select text → ask AI" functionality

**Decision**: Implement via JavaScript event listeners on the frontend that capture selected text and send it to the backend API

**Rationale**: Straightforward implementation using standard web APIs. The selection can be captured client-side and sent with the query to provide context to the backend.

**Alternatives considered**:
- Browser extension: Too complex for this use case
- Custom text editor component: Unnecessary complexity

### 5. Build Optimization Research

**Task**: Research how to ensure build times stay under 2 minutes

**Decision**: Optimize Docusaurus build configuration, limit image sizes, use efficient plugins, and consider pre-building content where possible

**Rationale**: Docusaurus is generally fast to build. Optimization techniques include image compression, code splitting, and caching. GitHub Actions can be used for CI/CD.

**Alternatives considered**:
- Static site generators like Gatsby: More complex for this use case
- Pre-rendering services: Might add unnecessary complexity

## Open Questions & Decisions

### 1. Frontend/Backend Architecture

**Question**: Should frontend and backend be in separate repositories or a monorepo?

**Decision**: Use monorepo approach with separate directories for frontend and backend.

**Rationale**: Easier to manage dependencies, versions, and deployment. Both parts can be developed and deployed in coordination.

### 2. Embedding Strategy

**Question**: How to generate embeddings for the textbook content?

**Decision**: Create a preprocessing pipeline that runs during content updates to generate and store embeddings in Qdrant.

**Rationale**: Pre-generating embeddings ensures fast query times and allows for better control over the embedding process. The pipeline can run in the CI/CD process when content changes.

### 3. Authentication & User Tracking

**Question**: Is authentication required for the textbook access?

**Decision**: No authentication required for basic textbook access; implement anonymous tracking for analytics only if needed.

**Rationale**: The textbook is designed for public access to students. Authentication would complicate the user experience and may not be necessary for the core functionality.

## Next Steps

1. Create data model based on the research findings
2. Design the API contracts for the RAG functionality
3. Set up the basic project structure
4. Create detailed implementation tasks