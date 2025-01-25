from transformers import pipeline, AutoProcessor
from PIL import Image


class VisionModel:
    def __init__(self):
        self.model_id = "llava-hf/llava-interleave-qwen-0.5b-hf"
        self.processor = None
        self.pipe = None

    def initialize(self):
        if self.processor is None:
            self.processor = AutoProcessor.from_pretrained(self.model_id)
            self.pipe = pipeline(
                "image-to-text", model=self.model_id, device_map="auto"
            )

    def process_image(self, image: Image.Image, prompt: str) -> str:
        if not self.processor:
            self.initialize()

        outputs = self.pipe(
            image, prompt=prompt, generate_kwargs={"max_new_tokens": 200}
        )
        return outputs[0]["generated_text"]
