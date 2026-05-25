import gradio as gr

from app.config.model_config import (
    AVAILABLE_MODELS
)

from app.services.code_generator_service import (
    CodeGeneratorService
)


TARGET_LANGUAGES = [
    "cpp",
    "rust",
    "javascript"
]


def generate_code_ui(
    source_code,
    target_language,
    selected_models
):

    if not source_code.strip():

        return "Please enter Python code."

    if not selected_models:

        return "Please select at least one model."

    results = []

    for model_key in selected_models:

        response = (
            CodeGeneratorService.generate_code(
                model_key=model_key,
                target_language=target_language,
                source_code=source_code
            )
        )

        if response.success:

            result_text = f"""
MODEL: {response.model_name}

PROVIDER: {response.provider}

GENERATION TIME: {response.generation_time} sec

SAVED FILE:
{response.saved_file_path}

GENERATED CODE:

{response.generated_code}
"""

        else:

            result_text = f"""
MODEL: {model_key}

ERROR:
{response.error}
"""

        results.append(result_text)

    return "\n\n" + ("=" * 80).join(results)


def create_ui():

    model_choices = list(
        AVAILABLE_MODELS.keys()
    )

    interface = gr.Interface(

        fn=generate_code_ui,

        inputs=[

            gr.Code(
                label="Python Source Code",
                language="python",
                lines=20
            ),

            gr.Dropdown(
                choices=TARGET_LANGUAGES,
                value="cpp",
                label="Target Language"
            ),

            gr.CheckboxGroup(
                choices=model_choices,
                value=["gemini_flash"],
                label="Select Models"
            )
        ],

        outputs=gr.Textbox(
            label="Generated Output",
            lines=30
        ),

        title="AI Code Generator",

        description="""
Convert Python code into other programming languages using multiple AI models.
""",

    )

    return interface