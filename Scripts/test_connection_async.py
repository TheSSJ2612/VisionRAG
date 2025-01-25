import asyncio
import sys
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

# Windows-specific event loop policy fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def test_connection():
    DATABASE_URL = "postgresql+psycopg_async://aivision:password@localhost:5432/maindb"

    try:
        engine = create_async_engine(DATABASE_URL)
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print(f"SQLAlchemy connection successful! Result: {result.scalar()}")
        await engine.dispose()
    except Exception as e:
        print(f"SQLAlchemy connection failed: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_connection())
