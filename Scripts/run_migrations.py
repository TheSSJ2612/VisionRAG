import asyncio
import sys
from api.src.core.database import init_db


async def main():
    await init_db()
    print("Database migrations completed successfully!")


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
