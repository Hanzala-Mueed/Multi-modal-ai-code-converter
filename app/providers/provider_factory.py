from app.providers.gemini_provider import GeminiProvider
from app.providers.ollama_provider import OllamaProvider
from app.providers.openrouter_provider import OpenRouterProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider_name: str, model_name: str):

        if provider_name == "gemini":
            return GeminiProvider(model_name)

        elif provider_name == "ollama":
            return OllamaProvider(model_name)

        elif provider_name == "openrouter":
            return OpenRouterProvider(model_name)

        else:
            raise ValueError(
                f"Unsupported provider: {provider_name}"
            )