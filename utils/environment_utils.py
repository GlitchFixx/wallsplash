import os

from exceptions.environment_variable_error import EnvironmentVariableNotFoundError
from utils.contextual_logger import ContextualLogger
from dotenv import load_dotenv

logger = ContextualLogger(logger_name=__name__)
load_dotenv()


def get_environment_variable(env_variable: str) -> str:
    """
    Retrieve the value of an environment variable.

    Args:
        env_variable (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Raises:
        EnvironmentVariableError: If the environment variable is not found.
    """

    value = os.getenv(env_variable)
    if value is None:
        logger.error(f"Environment variable {env_variable} not found")
        raise EnvironmentVariableNotFoundError(environment_variable=env_variable)
    return value
