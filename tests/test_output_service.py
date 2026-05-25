import os
import sys

# Find the absolute path of the project root (one level up from /tests)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.services.output_service import (
    OutputService
)


sample_code = """
#include <iostream>

int main() {
    std::cout << "Hello";
}
"""


saved_path = OutputService.save_generated_code(
    generated_code=sample_code,
    target_language="cpp",
    model_key="gemini_flash"
)

print(saved_path)