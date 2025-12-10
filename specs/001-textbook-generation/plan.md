# Implementation Plan: Physical AI & Humanoid Robotics Textbook

**Branch**: `001-textbook-generation` | **Date**: 2025-12-10 | **Spec**: [link to spec.md]
**Input**: Feature specification from `/specs/001-textbook-generation/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a Docusaurus-based textbook with 6 chapters on Physical AI & Humanoid Robotics, integrated with a RAG chatbot using Qdrant, Neon, and FastAPI. The system must provide clean UI, support select-text-to-ask functionality, and operate within free-tier resource constraints with minimal GPU usage.

## Technical Context

**Language/Version**: Python 3.11 (for FastAPI backend), JavaScript/TypeScript (for Docusaurus frontend), SQL (for Neon database)
**Primary Dependencies**: Docusaurus, FastAPI, Qdrant, Neon, OpenAI or similar LLM API, LangChain or LlamaIndex for RAG functionality
**Storage**: Neon PostgreSQL database for metadata, Qdrant vector database for embeddings, GitHub Pages for static hosting
**Testing**: pytest for backend, Jest for frontend, integration tests for RAG accuracy
**Target Platform**: Web application (frontend on GitHub Pages, backend API on free-tier hosting)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Build time under 2 minutes, RAG response time under 5 seconds, 99% uptime during peak hours
**Constraints**: Free-tier resource limits, minimal GPU usage, lightweight embeddings, GitHub Pages deployment
**Scale/Scope**: Support for multiple concurrent students, 6 textbook chapters, RAG functionality for all textbook content

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Initial Check (Pre-Design)
Based on the constitution file, the following principles must be met:
- Simplicity: Code and UI must be simple and clear
- Accuracy: Technical content and RAG responses must be accurate
- Minimalism: Features should be minimal and focused
- Fast Builds: Build process must complete under 2 minutes
- Free-tier Architecture: All services must work within free-tier constraints
- RAG Integrity: Chatbot must only provide answers based on textbook content

### Post-Design Check (Post-Phase 1)
Confirming adherence to constitutional principles after design phase:

- ✅ Simplicity: The design uses established frameworks (Docusaurus, FastAPI) to maintain simplicity
- ✅ Accuracy: RAG implementation will ensure responses are based on textbook content
- ✅ Minimalism: The architecture focuses on essential components only
- ✅ Fast Builds: Docusaurus build process can be optimized to meet 2-minute requirement
- ✅ Free-tier Architecture: All selected technologies (Qdrant, Neon, FastAPI) have free-tier options
- ✅ RAG Integrity: API contracts enforce source chapter referencing to prevent hallucinations

## Project Structure

### Documentation (this feature)

```text
specs/001-textbook-generation/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Structure Decision**: Web application structure with separate frontend (Docusaurus) and backend (FastAPI) components to allow static hosting of frontend while maintaining API functionality for RAG chatbot.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
