import urllib.request
import os

from constants.file_constants import FileConstants
# from service.wallpaper_manager import WallpaperManager
from utils.contextual_logger import ContextualLogger
from typing import List

from pydantic import ValidationError
from dto.image_response_dto import ImageResponseDTO

"""
 Manage image batch operations
    - Map image response to DTO
    - Batch download images
    - Batch cleanup images
    - Delete files
    - 
"""
class ImageOperationService:
    def __init__(self):
        self.__logger = ContextualLogger(logger_name=__name__)
        # self.__wallpaper_manager = WallpaperManager(self)

    @staticmethod
    def map_image_response_to_dto(response: List[dict]) -> List[ImageResponseDTO]:
        image_dtos = []
        for image_data in response:
            try:
                image_dto = ImageResponseDTO()  # Extract only URLs
                image_dto.id = image_data["id"]
                image_dto.url = image_data.get("urls", {}).get("raw")
                image_dtos.append(image_dto)

            except ValidationError as e:
                print(f"Error parsing image data: {e}")
        print(image_dtos)
        return image_dtos

    def batch_image_download(self, image_response: List[ImageResponseDTO]):
        images = []
        for image_info in image_response:
            image = image_info.id + FileConstants.JPEG_FORMAT
            output_dir: str = FileConstants.FILE_PATH + image
            image_url = image_info.url
            images.append(image)
            self.__save_image_to_folder(image_url, output_dir)
        #  FIXME: fix this
        from service.wallpaper_manager import WallpaperManager
        wallpaper_manager = WallpaperManager()
        wallpaper_manager.add_images_to_store(images)
        # self.delete_oldest_images(threshold=Constants.DEQUE_MAX_LENGTH)

    def __save_image_to_folder(self, image_url, output_dir):
        self.__logger.info(f"Download: File '{output_dir}' has been downloaded successfully.")
        urllib.request.urlretrieve(image_url, output_dir)

    def delete_file(self, file_path: str) -> None:
        """Deletes a single file if it exists."""
        file_path = FileConstants.FILE_PATH + file_path
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                self.__logger.info(f"Delete: File '{file_path}' has been deleted successfully.")
            except Exception as e:
                self.__logger.info(f"An error occurred while deleting '{file_path}': {e}")
        else:
            self.__logger.info(f"File '{file_path}' does not exist.")

    def batch_delete_images(self, images: List[str]):
        """Deletes a batch of image files specified by their file paths."""
        for image in images:
            self.delete_file(image)

    def cleanup(self, threshold: int):
        """
        Deletes the oldest images if the number of images exceeds the threshold.
        """
        image_files = sorted(
            [f for f in os.listdir(FileConstants.FILE_PATH) if f.endswith(FileConstants.JPEG_FORMAT)],
            key=lambda x: os.path.getctime(os.path.join(FileConstants.FILE_PATH, x))
        )
        images_to_delete = image_files[:len(image_files) - threshold]
        self.batch_delete_images(images_to_delete)