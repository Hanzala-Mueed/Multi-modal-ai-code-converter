from openai import OpenAI

from app.providers.base_provider import BaseProvider
from app.config.settings import settings

class OpenRouterProvider(BaseProvider):

    def __init__(self, model_name: str):

        self.model_name = model_name
        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    def generate_code(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model_name,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content