from service.image_operation_service import ImageOperationService
from service.wallpaper_manager import WallpaperManager
from utils.contextual_logger import ContextualLogger

logger = ContextualLogger(logger_name=__name__)

def main():
    image_operation_service = ImageOperationService()
    wallpaper_manager = WallpaperManager(image_operation_service)
    wallpaper_manager.get_wallpaper()


main()




# wallpaper_changer/                # Root of your project
# │
# ├── wallpaper_changer/            # Main package
# │   ├── __init__.py               # Marks this directory as a Python package
# │   ├── main.py                   # Main script to start the wallpaper changing process
# │   ├── api_client.py             # Handles API requests to download images
# │   ├── wallpaper_manager.py      # Handles wallpaper setting, image deletion, and scheduling
# │   ├── utils.py                  # Utility functions (like time calculation, logging, etc.)
# │
# ├── config/                       # Configuration files
# │   ├── config.json               # Stores API keys, image folder paths, and other settings
# │
# ├── images/                       # Directory where downloaded images will be stored temporarily
# │
# ├── logs/                         # Directory for log files
# │   ├── wallpaper_changer.log     # Log file to track downloads, deletions, errors, etc.
# │
# ├── tests/                        # Unit and integration tests
# │   ├── test_api_client.py        # Test API client functionality
# │   ├── test_wallpaper_manager.py # Test wallpaper management logic
# │
# ├── launch_agent/                 # macOS launch agent files (for running the script as a background service)
# │   ├── com.username.wallpaperchanger.plist  # macOS plist to run the script at startup
# │
# ├── README.md                     # Documentation for your project
# ├── requirements.txt              # List of Python dependencies
# └── setup.py                      # If you package this project for distribution or installation



