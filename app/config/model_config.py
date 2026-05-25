AVAILABLE_MODELS = {

    # =========================
    # Gemini Models
    # =========================

    "gemini_flash": {
        "provider": "gemini",
        "model_name": "gemini-2.5-flash",
        "display_name": "Gemini 2.5 Flash",
        "type": "cloud"
    },

    # =========================
    # OpenRouter Models
    # =========================

    "gpt_oss_free": {
        "provider": "openrouter",
        "model_name": "openai/gpt-oss-20b:free",
        "display_name": "GPT OSS 20B Free",
        "type": "cloud"
    },

    # =========================
    # Ollama Local Models
    # =========================

    "qwen_local": {
        "provider": "ollama",
        "model_name": "qwen3.5:0.8b",
        "display_name": "Qwen 3.5 0.8B",
        "type": "local"
    },

    "deepseek_coder_local": {
        "provider": "ollama",
        "model_name": "deepseek-coder:1.3b",
        "display_name": "DeepSeek Coder 1.3B",
        "type": "local"
    },

    "deepcoder_local": {
        "provider": "ollama",
        "model_name": "deepcoder:1.5b",
        "display_name": "DeepCoder 1.5B",
        "type": "local"
    }
}