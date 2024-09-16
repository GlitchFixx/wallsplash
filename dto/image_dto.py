from typing import List

from pydantic import BaseModel, Field


class ImageDTO(BaseModel):
    images: List[str] = Field(
        default=[],
        strict=True,
        description="List of image urls"
    )
