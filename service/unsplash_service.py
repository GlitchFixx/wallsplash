from constants.api_constants import ApiConstants
from dto.image_request_dto import ImageRequestDTO
from service.image_operation_service import ImageOperationService
from utils.contextual_logger import ContextualLogger
import requests

from utils.environment_utils import get_environment_variable
from utils.url_builder import URLBuilder


class UnsplashService:
    def __init__(self, image_operation_service):
        self.__logger = ContextualLogger(logger_name=__name__)
        self.__client_id = get_environment_variable('CLIENT_ID')
        self.__image_operation_service = image_operation_service

    def get_random_image(self, image_request_dto: ImageRequestDTO):
        try:
            params: dict = image_request_dto.model_dump()
            params["client_id"] = self.__client_id
            url = (
                URLBuilder(base_url=ApiConstants.UNSPLASH_BASE_API)
                .add_path(path=ApiConstants.GET_RANDOM_IMAGE_PREFIX)
                .add_query_parameters(params)
                .build()
            )
            self.__logger.info(f"URL: {url}")
            response = requests.get(url)
            # self.__logger.info(f"Response: {response.json()}")
            response_data = response.json()
            for item in response_data:
                log_entry = {
                    'id': item.get('id'),
                    'slug': item.get('slug'),
                    'urls': item.get('urls', {}).get('raw')
                }
                self.__logger.info(f"Response: {log_entry}")
            image_response = self.__image_operation_service.map_image_response_to_dto(response.json())
            if image_response:
                self.__image_operation_service.batch_image_download(image_response)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.__logger.error(f"Error requesting image: {e}")
            return None
        return response.json()
