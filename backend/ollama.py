"""Ollama API client for making local LLM requests."""

import httpx
import json
import logging
from typing import List, Dict, Any, Optional
from .config import OLLAMA_API_URL

logger = logging.getLogger("backend.ollama")

async def query_model(
    model: str,
    messages: List[Dict[str, str]],
    timeout: float = 300.0
) -> Optional[Dict[str, Any]]:
    """
    Query a single model via local Ollama API.

    Args:
        model: Ollama model identifier (e.g., "llama3")
        messages: List of message dicts with 'role' and 'content'
        timeout: Request timeout in seconds

    Returns:
        Response dict with 'content', or None if failed
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                OLLAMA_API_URL,
                json=payload
            )
            response.raise_for_status()

            data = response.json()
            message = data.get('message', {})

            return {
                'content': message.get('content'),
            }

    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error querying local model {model}: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        import traceback
        logger.error(f"Unexpected error querying local model {model}: {e}")
        logger.error(traceback.format_exc())
        return None


async def query_models_parallel(
    models: List[str],
    messages: List[Dict[str, str]]
) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Query multiple models in parallel.

    Args:
        models: List of Ollama model identifiers
        messages: List of message dicts to send to each model

    Returns:
        Dict mapping model identifier to response dict (or None if failed)
    """
    import asyncio

    # Create tasks for all models
    tasks = [query_model(model, messages) for model in models]

    # Wait for all to complete
    responses = await asyncio.gather(*tasks)

    # Map models to their responses
    return {model: response for model, response in zip(models, responses)}
