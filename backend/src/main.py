from fastapi import FastAPI
from src.api.chapter_routes import chapter_router
from src.api.chatbot_routes import chatbot_router
from src.api.session_routes import session_router

app = FastAPI(
    title="Physical AI & Humanoid Robotics Textbook API",
    description="API for textbook content and RAG chatbot functionality",
    version="0.1.0"
)

# Include API routers
app.include_router(chapter_router, prefix="/api/textbook", tags=["textbook"])
app.include_router(chatbot_router, prefix="/api/chatbot", tags=["chatbot"])
app.include_router(session_router, prefix="/api/session", tags=["session"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Textbook API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)