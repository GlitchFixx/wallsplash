from typing import Dict

from pydantic import BaseModel, Field


class  ImageResponseDTO(BaseModel):
    id: str = Field(
        default="",
        strict=True,
        description="Id associated with image")

    url: str = Field(
        default="",
        strict=True,
        description="Raw image url")
