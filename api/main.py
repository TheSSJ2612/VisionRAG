import sys
import asyncio
import logging
from fastapi import FastAPI
from .src.core.database import init_db
from .src.routes.users import router as user_router
from .src.routes.ai import router as ai_router

# Windows event loop fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(
    title="AI Vision Backend",
    description="Multimodal AI Assistant with RAG capabilities",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger(__name__)
    try:
        await init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutting down")


app.include_router(ai_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1/users")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
