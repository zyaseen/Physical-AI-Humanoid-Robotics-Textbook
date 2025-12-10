<!-- SYNC IMPACT REPORT
Version Change: N/A -> 1.0.0
Modified Principles: N/A (New constitution)
Added Sections: All principles and sections for Physical AI & Humanoid Robotics textbook
Removed Sections: N/A
Templates Requiring Updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/*.md: ⚠ pending
- README.md: ⚠ pending
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics — Essentials Constitution

## Core Principles

### I. Simplicity
All textbook content and code examples must prioritize simplicity and clarity above advanced features. Each concept should be explained with minimal jargon and maximum accessibility for students. Complexity must be introduced gradually and only when absolutely necessary for understanding.

### II. Accuracy
All technical content, code samples, and explanations must be factually accurate and technically correct. Information must be verified against authoritative sources, tested in practice, and kept up-to-date with current technology standards. Erroneous or misleading information is strictly prohibited.

### III. Minimalism
Textbook chapters and features should follow minimalist design principles. Unnecessary content, redundant explanations, or overly verbose sections must be eliminated. Focus on essential concepts that provide maximum educational value with minimum cognitive overhead.

### IV. Fast Builds
The Docusaurus textbook build process must remain fast and efficient. Build times should not exceed reasonable limits (under 2 minutes for full rebuild). Heavy processing, oversized assets, or inefficient configurations that slow down builds are prohibited without explicit justification.

### V. Free-tier Architecture
All infrastructure and service choices must remain compatible with free-tier hosting solutions. This includes database services, vector storage, API usage, and computational resources. The RAG system must operate efficiently within free-tier resource constraints.

### VI. RAG Integrity
The RAG chatbot must only provide answers derived from the textbook content itself. External hallucinations, fabricated information, or responses outside the scope of book content are strictly forbidden. Answers must be traceable to specific chapters or sections.

## Technical Constraints

The project must maintain low computational resource usage with no heavy GPU requirements. Embeddings must be lightweight and optimized for cost-effective serving. Third-party dependencies should be limited to essential packages only. The system architecture must support smooth deployment to GitHub Pages.

## Development Workflow

All contributions must undergo rigorous testing of both textbook content accuracy and RAG functionality. Chapter additions require verification of corresponding RAG performance. Code examples must be tested in the target environment before merging. Documentation of setup and deployment procedures must remain current with each change.

## Governance

This constitution governs all development decisions for the Physical AI & Humanoid Robotics textbook. All pull requests and reviews must verify compliance with these principles. Deviations require explicit approval and documentation of trade-offs. This document follows semantic versioning (MAJOR.MINOR.PATCH format) with amendments requiring team consensus.

**Version**: 1.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10