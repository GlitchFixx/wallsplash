# import logging
import os
from datetime import datetime
#
# from colorama import Fore, Style
#
# logging.Logger.root.level = 3
#
#
# class ContextualLogger:
#     def __init__(self, logger_name: str) -> None:
#         # Initialize the logger
#         self.logger = logging.getLogger(logger_name)
#
#         # Set the log level from the environment variable or default to INFO
#         log_level = os.getenv("APPLICATION_LOG_LEVEL", "INFO").upper()
#         self.logger.setLevel(log_level)
#
#         # Add a StreamHandler to output logs to the terminal
#         if not self.logger.handlers:
#             handler = logging.StreamHandler()
#             formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#             handler.setFormatter(formatter)
#             handler.addFilter(ColorFilter())
#             self.logger.addHandler(handler)
#
#     def debug(self, message: str, custom_fields: dict = {}):
#         self.logger.debug(message, extra=custom_fields)
#         if not self.logger.isEnabledFor(logging.DEBUG):
#             self.logger.info(f"DEBUG: {message}", extra=custom_fields)
#
#     def info(self, message: str, custom_fields: dict = {}):
#         self.logger.info(message, extra=custom_fields)
#
#     def warning(self, message: str, custom_fields: dict = {}):
#         self.logger.warning(message, extra=custom_fields)
#
#     def error(self, message: str, custom_fields: dict = {}):
#         self.logger.error(message, extra=custom_fields)
#
#     def critical(self, message: str, custom_fields: dict = {}):
#         self.logger.critical(message, extra=custom_fields)
#
#
#
# class ColorFilter(logging.Filter):
#     def filter(self, record):
#         record.levelname = Fore.WHITE + record.levelname + Style.RESET_ALL
#         return True



import logging
from os import getenv

class ColorFilter(logging.Filter):
    """Custom filter to colorize log messages based on level."""

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[87m'
    WHITE = '\033[97m'
    RESET = '\033[37m'


    def filter(self, record):
        """Assigns color codes based on log level."""
        level_color = {
            logging.DEBUG: self.GREEN,
            logging.INFO: self.WHITE,
            logging.WARNING: self.YELLOW,
            logging.ERROR: self.RED,
            logging.CRITICAL: self.MAGENTA
        }.get(record.levelno, self.WHITE)  # Default to white for unknown levels
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        record.msg = f"{self.WHITE}{timestamp}{self.RESET} : {self.WHITE}{record.name}{self.RESET} - {level_color}{record.levelname}{self.RESET} - {self.GRAY}{record.msg}{self.RESET}"
        return True

class ContextualLogger:
    def __init__(self, logger_name: str) -> None:
        # Initialize the logger
        self.logger = logging.getLogger(logger_name)

        # Set the log level from the environment variable or default to INFO
        log_level = os.getenv("APPLICATION_LOG_LEVEL", "INFO").upper()
        log_level = "DEBUG"
        self.logger.setLevel(log_level)

        # Add a StreamHandler to output logs to the terminal with color filtering
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            handler.addFilter(ColorFilter())
            self.logger.addHandler(handler)

    def debug(self, message: str, custom_fields: dict = {}):
        self.logger.debug(message, extra=custom_fields)
        # if not self.logger.isEnabledFor(logging.DEBUG):
        #     self.logger.info(f"DEBUG: {message}", extra=custom_fields)

    def info(self, message: str, custom_fields: dict = {}):
        self.logger.info(message, extra=custom_fields)

    def warning(self, message: str, custom_fields: dict = {}):
        self.logger.warning(message, extra=custom_fields)

    def error(self, message: str, custom_fields: dict = {}):
        self.logger.error(message, extra=custom_fields)

    def critical(self, message: str, custom_fields: dict = {}):
        self.logger.critical(message, extra=custom_fields)

