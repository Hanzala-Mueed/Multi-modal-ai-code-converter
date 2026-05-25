from pathlib import Path

from app.utils.file_utils import FileUtils


BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "outputs"


class OutputService:

    EXTENSIONS = {
        "cpp": ".cpp",
        "rust": ".rs",
        "javascript": ".js"
    }

    @staticmethod
    def save_generated_code(
        generated_code: str,
        target_language: str,
        model_key: str
    ) -> str:


        # Create folder path
        language_dir = OUTPUT_DIR / target_language

        model_dir = language_dir / model_key

        FileUtils.create_directory(
            model_dir
        )

        # Create filename with timestamp
        timestamp = FileUtils.generate_timestamp()

        extension = OutputService.EXTENSIONS.get(
            target_language,
            ".txt"
        )

        filename = f"{timestamp}{extension}"

        file_path = model_dir / filename

        # Save file
        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(generated_code)

        return str(file_path)