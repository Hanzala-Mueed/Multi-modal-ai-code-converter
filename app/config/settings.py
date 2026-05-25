import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )


settings = Settings()