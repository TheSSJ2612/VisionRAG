from fastapi import APIRouter, File, UploadFile, HTTPException
from ..services.ai_service import AIService
from PIL import Image
import io
import logging
from typing import Optional

router = APIRouter()
ai_service = AIService()
logger = logging.getLogger(__name__)


@router.post("/process")
async def process_input(  # Added async
    user_id: int, text: Optional[str] = None, image: Optional[UploadFile] = File(None)
):
    try:
        input_data = {"text": text}

        if image:
            if image.content_type not in ["image/jpeg", "image/png"]:
                raise HTTPException(400, "Invalid image format")
            image_data = await image.read()
            input_data["image"] = Image.open(io.BytesIO(image_data))

        return await ai_service.process_input(user_id, input_data)

    except Exception as e:
        logger.error(f"Processing error: {str(e)}")
        raise HTTPException(500, "Internal server error") from e
