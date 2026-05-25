import os
import sys

# Find the absolute path of the project root (one level up from /tests)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.services.code_generator_service import (
    CodeGeneratorService
)


python_code = """
def add(a, b):
    return a + b

print(add(5, 3))
"""


response = CodeGeneratorService.generate_code(
    model_key="gemini_flash",
    target_language="cpp",
    source_code=python_code
)


print(response.model_dump())