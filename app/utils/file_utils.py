from pathlib import Path
from datetime import datetime


class FileUtils:

    @staticmethod
    def create_directory(path: Path):

        path.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def generate_timestamp() -> str:

        return datetime.now().strftime(
            "%Y_%m_%d_%H_%M_%S"
        )