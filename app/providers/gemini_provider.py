import google.generativeai as genai


from app.providers.base_provider import BaseProvider
from app.config.settings import settings


class GeminiProvider(BaseProvider):

    def __init__(self, model_name: str):

        self.model_name = model_name

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            model_name
        )

    def generate_code(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> str:

        final_prompt = f"""
        SYSTEM:
        {system_prompt}

        USER:
        {user_prompt}
        """

        response = self.model.generate_content(
            final_prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        )

        return response.text