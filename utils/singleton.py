class Singleton(type):
    """
    Metaclass for implementing the Singleton design pattern.

    The Singleton metaclass ensures that only one instance of a class is created and shared
    across all calls. This is achieved by maintaining a dictionary of instances for each class
    and reusing an existing instance if available.

    Usage:
    - Define a class with this metaclass to make it a Singleton.
    - Access the instance using ClassName() syntax.

    Example:
    class MyClass(metaclass=Singleton):
        # Class definition

    Attributes:
        __instances (dict): A dictionary to store instances of Singleton classes.
    """

    __instances: dict = {}

    def __call__(cls, *args, **kwargs):
        """
        Create and return an instance of the Singleton class.

        If an instance of the class already exists, return the existing instance.
        Otherwise, create a new instance and store it for future use.

        :param cls: The class being instantiated.
        :type cls: type
        :param args: Positional arguments for the class constructor.
        :param kwargs: Keyword arguments for the class constructor.
        :return: The instance of the Singleton class.
        :rtype: object
        """

        if cls not in cls.__instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            instance.__init__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]
