

class EnvironmentVariableNotFoundError(Exception):
    """
    Exception raised when a specific environment variable is not found.

    :param environment_variable: The name of the environment variable that was not found.
    :type environment_variable: str
    """

    def __init__(self, environment_variable: str) -> None:
        self.message = f"Environment variable {environment_variable} not found"
        super().__init__(self.message)
