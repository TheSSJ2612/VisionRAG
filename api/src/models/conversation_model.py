from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict


class ConversationBase(BaseModel):
    user_id: int
    messages: List[Dict[str, str]]
    timestamp: datetime = datetime.now()


class ConversationCreate(ConversationBase):
    pass


class Conversation(ConversationBase):
    id: int

    class Config:
        orm_mode = True
