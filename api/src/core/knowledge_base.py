from sqlalchemy.orm import Session
from sqlalchemy import func
from sentence_transformers import SentenceTransformer
from .database import SessionLocal, KnowledgeEntry  # Fixed import
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class KnowledgeRetriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.db = SessionLocal()

    def _format_results(self, results: List) -> List[Dict]:  # Added method
        return [
            {
                "content": result.KnowledgeEntry.content,
                "score": float(result.score),
                "source": result.KnowledgeEntry.source,
            }
            for result in results
        ]

    def retrieve_relevant_context(
        self, user_id: int, query: str, history: list
    ) -> List[Dict]:
        query_embedding = self.model.encode(query).tolist()

        common_results = (
            self.db.query(
                KnowledgeEntry,
                func.l2_distance(KnowledgeEntry.embedding, query_embedding).label(
                    "score"
                ),
            )
            .filter(KnowledgeEntry.scope == "common")
            .order_by("score")
            .limit(3)
            .all()
        )

        user_results = (
            self.db.query(
                KnowledgeEntry,
                func.l2_distance(KnowledgeEntry.embedding, query_embedding).label(
                    "score"
                ),
            )
            .filter(KnowledgeEntry.scope == str(user_id))
            .order_by("score")
            .limit(2)
            .all()
        )

        return self._format_results(common_results + user_results)

    def store_knowledge(self, user_id: int, content: str, source: str = "user") -> None:
        embedding = self.model.encode(content).tolist()
        entry = KnowledgeEntry(
            content=content, embedding=embedding, scope=str(user_id), source=source
        )
        self.db.add(entry)
        self.db.commit()
