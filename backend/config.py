"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# Ollama configuration
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")

# Council members - list of local Ollama model identifiers
COUNCIL_MODELS = [
    "qwen3:4b",
    "mistral:latest",
    "llama3.2:1b",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "deepseek-r1:1.5b"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
