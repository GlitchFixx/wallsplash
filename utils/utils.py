import os

class Utils:

    @staticmethod
    def get_file_count(directory):
        return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
