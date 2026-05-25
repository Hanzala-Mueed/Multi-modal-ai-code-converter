import os
import sys

# Find the absolute path of the project root (one level up from /tests)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.services.prompt_service import PromptService

prompt = PromptService.build_system_prompt(
    "cpp"
)

print(prompt)