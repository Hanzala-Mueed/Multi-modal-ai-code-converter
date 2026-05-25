import time
from app.config.model_config import AVAILABLE_MODELS
from app.models.response_models import (GenerationResponse)
from app.providers.provider_factory import (ProviderFactory)
from app.services.prompt_service import (PromptService)
from app.services.output_service import (OutputService)


class CodeGeneratorService:

    @staticmethod
    def generate_code(
        model_key: str,
        target_language: str,
        source_code: str
    ) -> GenerationResponse:

        try:

            # Load model config
            model_config = AVAILABLE_MODELS.get(
                model_key
            )

            if not model_config:
                raise ValueError(
                    f"Invalid model key: {model_key}"
                )

            provider_name = model_config["provider"]

            model_name = model_config["model_name"]

            # Create provider instance
            provider = ProviderFactory.get_provider(
                provider_name=provider_name,
                model_name=model_name
            )

            # Build system prompt
            system_prompt = (
                PromptService.build_system_prompt(
                    target_language
                )
            )

            # Generate code
            start_time = time.time()

            generated_code = provider.generate_code(
                system_prompt=system_prompt,
                user_prompt=source_code
            )

            end_time = time.time()

            generation_time = round(
                end_time - start_time,
                2
            )

            saved_file_path = (
                OutputService.save_generated_code(
                    generated_code=generated_code,
                    target_language=target_language,
                    model_key=model_key
                )
            )

            return GenerationResponse(
                provider=provider_name,
                model_name=model_name,
                target_language=target_language,
                generated_code=generated_code,
                success=True,
                generation_time=generation_time,
                saved_file_path=saved_file_path
            )
        


        except Exception as error:

            return GenerationResponse(
                provider="unknown",
                model_name="unknown",
                target_language=target_language,
                success=False,
                error=str(error)
            )
        
