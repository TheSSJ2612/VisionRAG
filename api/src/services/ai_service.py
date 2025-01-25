from transformers import pipeline, AutoProcessor
from api.src.core.config import settings
from api.src.core.database import AsyncSessionLocal
import logging

logger = logging.getLogger(__name__)


class AIService:
    def __init__(self):
        self.processor = None
        self.pipe = None
        self.db = AsyncSessionLocal()
        self.device = settings.model_device

    async def initialize_model(self):
        if self.processor:
            return "already initialized"

        try:
            model_id = "llava-hf/llava-interleave-qwen-0.5b-hf"
            self.pipe = pipeline(
                "image-to-text",
                model=model_id,
                device_map=self.device,
                torch_dtype="auto",
            )
            self.processor = AutoProcessor.from_pretrained(model_id)
            return "initialized successfully"
        except Exception as e:
            logger.error(f"Model initialization failed: {str(e)}")
            raise

    async def process_image(self, image, prompt: str):
        if not self.processor:
            await self.initialize_model()

        try:
            outputs = await self.pipe(
                image, prompt=prompt, generate_kwargs={"max_new_tokens": 200}
            )
            return outputs[0]["generated_text"]
        except Exception as e:
            logger.error(f"Image processing failed: {str(e)}")
            raise
