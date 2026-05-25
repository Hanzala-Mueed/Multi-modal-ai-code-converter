
import os
import sys

# Find the absolute path of the project root (one level up from /tests)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.providers.gemini_provider import GeminiProvider


provider = GeminiProvider(
    model_name="gemini-2.5-flash"
)

response = provider.generate_code(
    system_prompt="Convert Python code to C++",
    user_prompt="print('hello world')"
)

print(response)