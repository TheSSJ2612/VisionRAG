from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete  # Added import
from api.src.core.database import AsyncSessionLocal  # Fixed import
from api.src.models.user_model import UserCreate, User
from api.src.utils.security import get_password_hash
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        self.db = AsyncSessionLocal()

    async def delete_user(self, user_id: int) -> bool:  # Added method
        result = await self.db.execute(delete(User).where(User.id == user_id))
        await self.db.commit()
        return result.rowcount > 0
