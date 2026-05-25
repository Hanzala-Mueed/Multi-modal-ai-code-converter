import requests

from app.providers.base_provider import BaseProvider
from app.config.settings import settings

class OllamaProvider(BaseProvider):

    def __init__(self, model_name: str):

        self.model_name = model_name
        self.base_url = settings.OLLAMA_BASE_URL

    def generate_code(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> str:

        prompt = f"""
        SYSTEM:
        {system_prompt}

        USER:
        {user_prompt}
        """

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]