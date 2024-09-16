import random

from collections import deque
from typing import List, Deque, Optional

from constants.api_constants import ApiConstants
from constants.constants import Constants
from constants.file_constants import FileConstants
from dto.image_request_dto import ImageRequestDTO
from service.unsplash_service import UnsplashService
from utils.contextual_logger import ContextualLogger
from utils.singleton import Singleton
from utils.utils import Utils


#
class WallpaperManager(metaclass=Singleton):
    # Maintains image ids to efficiently download/remove images
    __store: Optional[Deque[str]] = None

    def __init__(self, image_operation_service):
        self.__logger = ContextualLogger(logger_name=__name__)
        self.__unsplash_service = UnsplashService(image_operation_service)
        self.__image_operation_service = image_operation_service
        if self.__store is None:
            self.__store = deque(maxlen=Constants.DEQUE_MAX_LENGTH)
        self._last_topic = None

    def get_store_size(self):
        return len(self.__store)

    def add_images_to_store(self, images: List[str]):
        """
        If store size is equal to or greater than DEQUE_MAX_LENGTH then
        remove the old images ids and delete the images
        """
        self.__store.extend(images)
        # if self.get_store_size() > 20:
        self.remove_images_from_store()

    def remove_images_from_store(self, image_count: int = 20):
        images = []
        self.__logger.info("Removing images")
        for _ in range(image_count):
            if self.__store:
                image = self.__store.pop()
                images.append(image)
                # self.__logger.info(f"Removing image : {image}")
        # TODO: Fix this
        # self.__image_operation_service.batch_delete_images(images)
        file_count = Utils.get_file_count(FileConstants.FILE_PATH)
        if file_count > Constants.DEQUE_MAX_LENGTH:
            self.__image_operation_service.cleanup(Constants.DEQUE_MAX_LENGTH)

    def get_wallpaper(self):
        random_topic = WallpaperManager.get_random_topic()
        while random_topic == self._last_topic:
            random_topic = WallpaperManager.get_random_topic()
        self._last_topic = random_topic
        self.__logger.info(f"Random topic: {random_topic}")
        image_request_param = ImageRequestDTO(query=random_topic)
        image_data = self.__unsplash_service.get_random_image(image_request_param)

    @staticmethod
    def get_random_topic():
        """
        Returns a random topic from the wallpaper topics.
        """
        return random.choice(ApiConstants.WALLPAPER_TOPIC)