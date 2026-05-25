from pydantic import BaseModel


class GenerationResponse(BaseModel):

    provider: str

    model_name: str

    generated_code: str

    target_language: str

    success: bool

    error: str | None = None