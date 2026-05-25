from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate_code(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 2048
    ) -> str:
        """
        Generate code using AI model.
        """
        pass