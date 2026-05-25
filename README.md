# Multi-Model AI Code Converter

An AI-powered code translation and evaluation platform that converts Python code into multiple programming languages using multiple AI providers and models.

The project supports:
- Gemini API
- Ollama local models
- OpenRouter models

The application provides a Gradio-based UI for generating and comparing code outputs from different AI models.

---

# Features

- Convert Python code into:
  - C++
  - Rust
  - JavaScript

- Multi-model generation
- Local + cloud model support
- Organized output saving system
- Gradio web interface
- Scalable provider architecture
- Prompt management system
- Evaluation-ready structure

---

# Project Structure

```text
multi-modal-ai-code-converter/
│
├── app/
│   ├── main.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── model_config.py
│   │
│   ├── providers/
│   │   ├── base_provider.py
│   │   ├── gemini_provider.py
│   │   ├── ollama_provider.py
│   │   └── openrouter_provider.py
│   │
│   ├── prompts/
│   │   ├── cpp_prompt.txt
│   │   ├── rust_prompt.txt
│   │   └── javascript_prompt.txt
│   │
│   ├── services/
│   │   ├── code_generator_service.py
│   │   ├── prompt_service.py
│   │   └── output_service.py
│   │
│   ├── ui/
│   │   └── gradio_ui.py
│   │
│   ├── models/
│   │   └── response_models.py
│   │
│   ├── utils/
│   │   ├── file_utils.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   └── outputs/
│       ├── cpp/
│       ├── rust/
│       └── javascript/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

# Supported Models

## Gemini

- gemini-2.5-flash

## OpenRouter

- openai/gpt-oss-20b:free

## Ollama

- qwen3.5:0.8b
- deepseek-coder:1.3b
- deepcoder:1.5b

---

# Gradio UI Interface

<img width="1338" height="606" alt="Screenshot 2026-05-25 080820" src="https://github.com/user-attachments/assets/33bb6684-99c7-4acb-b742-bdfab1402973" />

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Hanzala-Mueed/Multi-modal-ai-code-converter.git
cd Multi-modal-ai-code-converter
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Ubuntu / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key

OPENROUTER_API_KEY=your_openrouter_api_key

OLLAMA_BASE_URL=http://localhost:11434
```

---

# Ollama Setup

## Install Ollama

Download and install Ollama:

- Windows / Mac / Linux:
  https://ollama.com/download

---

## Start Ollama Server

```bash
ollama serve
```

---

## Pull Required Models

```bash
ollama pull qwen3.5:0.8b
```

```bash
ollama pull deepseek-coder:1.3b
```

```bash
ollama pull deepcoder:1.5b
```

---

## Verify Installed Models

```bash
ollama list
```

---

# Running the Project

Start the Gradio application:

```bash
python run.py
```

After running, open:

```text
http://127.0.0.1:7860
```

in your browser.

---

# How to Use

1. Enter Python code in the editor.
2. Select target programming language.
3. Select one or more AI models.
4. Click Generate.
5. View generated outputs.
6. Generated files are automatically saved inside:
   `app/outputs/`

---

# Output Structure

Generated code files are organized by:

- target language
- model name
- timestamp

Example:

```text
outputs/
   cpp/
      gemini_flash/
         2026_05_25_10_30_12.cpp

      qwen_local/
         2026_05_25_10_31_02.cpp
```

---

# Current Vol 1 Scope

## Included

- Multi-model code generation
- Provider abstraction
- Prompt management
- Output saving
- Gradio UI

## Not Included Yet

- Code compilation
- Code execution
- Docker sandboxing
- Benchmarking
- Automated testing
- Streaming responses

---

# Future Vol 2 Features

Planned future improvements:

- Code compilation
- Runtime execution
- Sandboxed execution
- AI evaluation scoring
- Benchmark comparisons
- Syntax validation
- Performance analysis
- Download generated files
- Advanced UI improvements

---

# Technologies Used

- Python
- Gradio
- Gemini API
- Ollama
- OpenRouter
- Pydantic
- Loguru

---
