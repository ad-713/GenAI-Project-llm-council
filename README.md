# LLM Council (Local Edition)

![llmcouncil](header.jpg)

This project is a refactor of the original LLM Council concept. Instead of relying on cloud-based models via OpenRouter, the entire system runs locally using [Ollama](https://ollama.com/). Multiple local LLMs collaborate by answering, reviewing, and synthesizing responses to a user query.

The council consists of several models that provide initial responses and then rank each other's work. A dedicated Chairman LLM then produces the final synthesized output.

## Modifications from the Original Project

- **Local Execution**: Migrated from OpenRouter (Cloud) to Ollama (Local).
- **Custom Ollama Client**: Implemented a dedicated client in `backend/ollama.py` to handle local model requests.
- **Setup Refactor**: Simplified the start process to work with standard Python/Conda environments, removing the strict dependency on `uv`.

## How it Works

1. **Stage 1: First opinions**. The user query is sent to all local council models (e.g., Qwen, Mistral, Llama).
2. **Stage 2: Review**. Each individual LLM is given the responses of the other LLMs. Under the hood, the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs. The LLM is asked to rank them in accuracy and insight.
3. **Stage 3: Final response**. The Chairman model (e.g., DeepSeek-R1) synthesizes all responses and peer rankings into a final comprehensive answer.

## Prerequisites

- [Ollama](https://ollama.com/) installed and running.
- Pull the required models:
  ```bash
  ollama pull deepseek-r1:1.5b
  ollama pull qwen3:4b
  ollama pull mistral:latest
  ollama pull llama3.2:1b
  ```

## Setup

### 1. Backend Setup

The project can be run in a Conda environment or using standard Python.

```bash
# 1. Create and activate environment
conda create -n llm-council python=3.10
conda activate llm-council

# 2. Install dependencies
pip install fastapi uvicorn httpx python-dotenv respx pytest-asyncio
```

### 2. Frontend Setup

```bash
cd frontend
npm install
cd ..
```

### 3. Configuration

Local models are defined in `backend/config.py`. You can adjust model names or the Ollama API URL (default: `http://localhost:11434/api/chat`).

## Running the Application

**Option 1: Using the Start Script**
```bash
./start.sh
```

**Option 2: Manual Start**

**Terminal 1 (Backend):**
```bash
# Ensure your environment is activated
python -m backend.main
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Running Tests

Verify the integration with:
```bash
# Ensure your environment is activated
python -m pytest backend/tests
```

## Tech Stack

- **Backend:** FastAPI, Ollama (Local API), Httpx
- **Frontend:** React + Vite, Tailwind CSS
- **Testing:** Pytest, Respx
- **Storage:** JSON-based conversation history
