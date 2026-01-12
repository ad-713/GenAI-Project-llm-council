# Technical Report: LLM Council Local Implementation

## 1. Project Overview
This project is a local implementation of the "LLM Council" architecture, originally developed by Andrej Karpathy. The core objective is to improve the quality of LLM outputs by using a multi-agent workflow consisting of generation, peer review, and final synthesis. Our implementation focuses on privacy, cost-efficiency, and local control by migrating the system to use **Ollama**.

## 2. Key Design Decisions

### Local-First Architecture
The most significant design decision was the removal of cloud dependencies. By using Ollama as the backend provider, we ensure that:
- **Data Privacy**: All prompts and responses remain on the local machine.
- **Cost**: No API usage fees or token-based billing.
- **Latency**: No network round-trips to external API providers (limited only by local hardware performance).

### Backend Refactoring
We replaced the original OpenRouter-based client with a custom `OllamaClient` (implemented in `backend/ollama.py`). This client uses `httpx` for asynchronous communication with the local Ollama API, allowing for efficient parallel processing of council member responses.

### Anonymized Peer Review
To prevent bias in the review stage (Stage 2), we maintain the original design's "blind review" process. Models are presented with responses without knowing which model produced them, forcing them to judge based on content quality rather than model reputation.

## 3. Chosen LLM Models
The council is composed of diverse models to ensure a variety of perspectives. The default configuration includes:

- **Council Members**:
    - `qwen3:4b`: Chosen for its efficiency and strong performance in logical reasoning for its size.
    - `mistral:latest`: A reliable general-purpose model with balanced performance.
    - `llama3.2:1b`: A lightweight model used to demonstrate the system's ability to incorporate smaller, faster agents.
- **Chairman**:
    - `deepseek-r1:8b`: Selected as the Chairman for its advanced reasoning capabilities and "Chain-of-Thought" processing, making it ideal for synthesizing multiple viewpoints into a coherent final answer.

## 4. Improvements Over Original Repository

### 1. Local Integration
While the original repository was built for cloud APIs, this version is fully integrated with the Ollama ecosystem. We added automated handling for local model endpoints and simplified the configuration for local model identifiers.

### 2. Dependency Management & Portability
- **Simplified Setup**: Refactored the installation process to work with standard Python environments and Conda, reducing the friction found in the original `uv`-centric setup.

### 3. Asynchronous Optimization
The backend was optimized to handle multiple local model queries in parallel using Python's `asyncio`. This is critical for local execution where model loading and inference can be resource-intensive; parallelizing the wait times for inference significantly improves the user experience.

### 4. Robust Error Handling
Implemented better logging and error recovery in the `backend/ollama.py` client to handle common local issues, such as models not being pulled or the Ollama service being unavailable.

## 5. Use of Generative AI
Generative AI tools were used in the development and documentation of this project. **Gemini 3 Flash** and **Gemini 3 Pro** from **Google Gemini API** were utilized to assist in:
- **Code Refactoring**: Streamlining the transition from cloud-based APIs to a local Ollama implementation and optimizing asynchronous communication patterns.
- **Documentation Writing**: Drafting and refining technical documentation, including this report and the project's README, to ensure clarity, consistency, and professional quality.
