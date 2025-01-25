from sqlalchemy.orm import Session
from sqlalchemy import select  # Added import
from ..core.database import SessionLocal, Conversation  # Fixed import
import json


class MemoryManager:
    def __init__(self):
        self.db = SessionLocal()

    def get_conversation_history(self, user_id: int, limit: int = 10):
        return (
            self.db.execute(
                select(Conversation)
                .filter_by(user_id=user_id)
                .order_by(Conversation.created_at.desc())
                .limit(limit)
            )
            .scalars()
            .all()
        )

    def update_conversation(self, user_id: int, message_pair: dict):
        try:
            conv = Conversation(user_id=user_id, messages=json.dumps(message_pair))
            self.db.add(conv)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise

    def __del__(self):
        self.db.close()
