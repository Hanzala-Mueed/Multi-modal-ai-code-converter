from pydantic import BaseModel


class GenerationResponse(BaseModel):

    provider: str

    model_name: str

    target_language: str

    generated_code: str = ""

    success: bool

    error: str | None = None

    generation_time: float | None = None

    saved_file_path: str | None = None