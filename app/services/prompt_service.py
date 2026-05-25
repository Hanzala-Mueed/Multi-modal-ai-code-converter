from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"

class PromptService:

    @staticmethod
    def load_prompt_file(filename: str) -> str:

        file_path = PROMPTS_DIR / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def build_system_prompt(
        target_language: str
    ) -> str:

        generic_rules = PromptService.load_prompt_file(
            "generic_rules.txt"
        )

        language_prompt_file = f"{target_language}_prompt.txt"

        language_rules = PromptService.load_prompt_file(
            language_prompt_file
        )

        final_prompt = f"""
        {generic_rules}

        {language_rules}
        """

        return final_prompt.strip()