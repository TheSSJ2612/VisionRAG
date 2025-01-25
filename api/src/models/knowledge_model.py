from pydantic import BaseModel
from datetime import datetime


class KnowledgeBase(BaseModel):
    content: str
    embedding: list
    scope: str  # 'common' or user_id
    source: str = "user"
    timestamp: datetime = datetime.now()


class KnowledgeCreate(KnowledgeBase):
    pass


class Knowledge(KnowledgeBase):
    id: int

    class Config:
        orm_mode = True
