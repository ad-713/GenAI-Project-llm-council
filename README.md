# LLM Council (Ollama Local Edition)

![llmcouncil](header.jpg)

**Author:** Adrien GREVET
**Project Group:** CDOF3  
**Project Base:** Fork of [karpathy/llm-council](https://github.com/karpathy/llm-council)

## Project Overview

LLM Council is a collaborative multi-model system where different Large Language Models (LLMs) work together to provide high-quality answers. Instead of relying on a single model, the system leverages a "council" of models that generate initial opinions and review each other's work. A final "Chairman" model synthesizes these diverse perspectives and peer evaluations into a single, comprehensive response.

This fork migrates the original cloud-based architecture (OpenRouter) to a fully local execution environment using **Ollama**.

## How it Works

The process follows a three-stage workflow:

1.  **Stage 1: First Opinions**: The user query is sent to multiple local models (e.g., Qwen, Llama, Mistral).
2.  **Stage 2: Peer Review**: Each model reviews the responses from Stage 1. Identities are anonymized to ensure unbiased ranking based on accuracy and insight.
3.  **Stage 3: Synthesis**: A Chairman model (e.g., DeepSeek-R1) receives all initial responses and the peer reviews to produce the final, definitive answer.

## Setup and Installation

### Prerequisites

*   **Ollama**: Install it from [ollama.com](https://ollama.com/).
*   **Python 3.10+**
*   **Node.js & npm**

### 1. Model Preparation

Pull the models used in the default configuration:

```bash
ollama pull deepseek-r1:8b
ollama pull qwen3:4b
ollama pull mistral:latest
ollama pull llama3.2:1b
```

### 2. Backend Setup

It is recommended to use a virtual environment (Conda):

```bash
# Create and activate environment
conda create -n llm-council python=3.10
conda activate llm-council

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend
npm install
cd ..
```

## Running the Demo

You can run the entire application using the provided script or manually in two terminals.

### Option 1: Using the Start Script

```bash
./start.sh
```

### Option 2: Manual Execution

**Terminal 1 (Backend):**
```bash
# Ensure environment is activated
python -m backend.main
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

The application will be available at [http://localhost:5173](http://localhost:5173).

## Benchmarking Model Strength

This project can serve as a live demonstration of how model size and architecture impact performance. By using a diverse council of models, the system highlights:

*   **Performance Variability**: Observe how models with different parameter counts handle the same prompt, from lightweight models to larger reasoning-optimized ones.
*   **Reasoning Gap**: The multi-stage workflow exposes how larger models are often better equipped to identify errors (in Stage 2) and synthesize complex information (in Stage 3) compared to their smaller counterparts.
*   **Collaborative Synergy**: See how a "Chairman" model can leverage the collective input of multiple models to produce a result that exceeds the capabilities of any single small model.

## Technical Features

*   **Local-First**: No API keys or cloud costs; data stays on your machine.
*   **Parallel Processing**: Council opinions are gathered simultaneously for better performance.
*   **Extensible**: Easily swap models in `backend/config.py`.
