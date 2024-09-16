from typing import List, Dict

from constants.constants import SEPARATOR


class URLBuilder:
    """
    This class facilitates the construction of URLs by allowing the addition of path parts,
    path variables, and query parameters using the builder pattern.

    Attributes:

    __base_url (str): The base URL for the constructed URL.
    __path_parts (list): List of path parts to be combined.
    __path_variables (dict): Dictionary containing path variables and their values.
    __query_parameters (dict): Dictionary containing query parameters and their values.

    Example:
    base_url = "https://example.com"
    url_builder = URLBuilder(base_url)
    url = url_builder.add_path("api").add_path_variable("user_id", 123).add_path("users").build()
    print(url)  # Output: "https://example.com/api/123/users"
    """

    def __init__(self, base_url):
        """
        Initialize a new URLBuilder instance.

        Args:
            base_url (str): The base URL for the URL construction.

        """
        self.__base_url: str = base_url
        self.__path_parts: List[str] = []
        self.__path_variables: dict = {}
        self.__query_parameters: dict = {}

    def add_path(self, path) -> "URLBuilder":
        """
        Add a path part to the URL construction.

        Args:
            path (str): The path part to be added to the URL.

        Returns:
            URLBuilder: Returns the current URLBuilder instance for method chaining.

        """
        self.__path_parts.append(path)
        return self

    def add_path_variable(self, key, value) -> "URLBuilder":
        """
        Add a path variable and its value to the URL construction.

        Args:
            key (str): The key or name of the path variable.
            value (str): The value to be replaced for the path variable.

        Returns:
            URLBuilder: Returns the current URLBuilder instance for method chaining.

        """
        self.__path_variables[key] = value
        return self

    def add_query_parameter(self, key, value) -> "URLBuilder":
        """
        Add a query parameter and its value to the URL construction.
        Args:
            key (str): The key of the query parameter.
            value (str): The value of the query parameter.
        Returns:
            URLBuilder: Returns the current URLBuilder instance for method chaining.
        """
        self.__query_parameters[key] = value
        return self

    def add_query_parameters(self, params: Dict[str, str]) -> "URLBuilder":
        """
        Add multiple query parameters and their values to the URL construction.
        Args:
            params (dict): A dictionary containing query parameters and their values.
        Returns:
            URLBuilder: Returns the current URLBuilder instance for method chaining.
        """
        self.__query_parameters.update(params)
        return self


    def build(self) -> str:
        """
        Build and return the final URL based on the added components.
        Returns:
            str: The constructed URL.
        """
        path: str = SEPARATOR.EMPTY_STRING.join(self.__path_parts).format(**self.__path_variables)
        url: str = self.__base_url + path

        if self.__query_parameters:
            query_string = SEPARATOR.AMPERSAND.join(
                f"{key}={value}" for key, value in self.__query_parameters.items()
            )
            url += SEPARATOR.QUESTION_MARK + query_string

        return url
