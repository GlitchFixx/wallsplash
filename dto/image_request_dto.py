from typing import Dict

from pydantic import BaseModel, Field


class ImageRequestDTO(BaseModel):
    """
    Pydantic model representing parameters for the Unsplash random photo API.
    """

    orientation: str = Field(default="landscape")
    query: str = Field(default="Beach", description="Search key words") # Macro Moments
    count: int = Field(default=10, description="Count of images")
    h: int = Field(default=2160, description="Height of image", alias='height')
    w: int = Field(default=3840, description="Width of image", alias='width')
    auto: str = Field(default="enhance", description="Automate a baseline level of optimization")
    fit: str = Field(default="fill", description="Resizes the image to fit to its target dimensions")
    fill: str = Field(default="gen", description="Fill the excess space in an resized image")  # gen, blur, solid
    fill_color: str = Field(default="black", description="Color to use for fill param")
    upscale: bool = Field(default=True, description="Upscale the quality of the image")
    # dpr: int = 10
