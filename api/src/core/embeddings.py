from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_embedding(self, text: str) -> list:
        """Generate embedding for text using SBERT model"""
        return self.model.encode(text).tolist()

    def batch_embed(self, texts: list) -> list:
        """Generate embeddings in batch"""
        return [self.generate_embedding(text) for text in texts]
