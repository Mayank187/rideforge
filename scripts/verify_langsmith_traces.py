"""
verify_langsmith_traces.py

Utility script to verify that LangSmith tracing is correctly configured and
operational with the local Ollama LLM backend. Run this script directly to
perform a quick end-to-end smoke test of the tracing pipeline.
"""

import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

# Load environment variables from .env file, overriding any existing shell vars
load_dotenv(override=True)


def verify_langsmith_traces() -> None:
    """Verify LangSmith tracing is working correctly with the Ollama client.

    Performs three steps:
    1. Prints the current LangSmith environment configuration for inspection.
    2. Initialises a ChatOllama client with tracing metadata attached.
    3. Sends a sample prompt and prints the raw response to confirm a trace
       was generated and the model is reachable.
    """
    # --- Environment variable check ---
    # Print the key LangSmith settings so the caller can confirm they are set
    # before a trace attempt is made.
    print("LangSmith Tracing Enabled:", os.getenv("LANGSMITH_TRACING"))
    print("LangSmith Endpoint:       ", os.getenv("LANGSMITH_ENDPOINT"))
    print("LangSmith API Key:        ", "Set" if os.getenv("LANGSMITH_API_KEY") else "Not Set")
    print("LangSmith Project:        ", os.getenv("LANGSMITH_PROJECT"))

    # --- Ollama client initialisation ---
    # Metadata fields are forwarded to LangSmith so each run appears under the
    # correct project and model name in the tracing dashboard.
    ollama_client = ChatOllama(
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        model=os.getenv("CHAT_MODEL", "gemma4:e2b"),
        metadata={
            "trace": True,
            "ls_model_name": os.getenv("CHAT_MODEL", "gemma4:e2b"),
            "project": os.getenv("LANGSMITH_PROJECT", "rideforge"),
        },
    )

    # --- Test invocation ---
    # A lightweight prompt is used so the round-trip is fast and the resulting
    # trace is easy to identify in the LangSmith UI.
    response = ollama_client.invoke(
        "Give me top 3 tips for a safe and enjoyable motorcycle trip."
    )
    print("Response from Ollama:", response)


if __name__ == "__main__":
    # Run the verification function when this script is executed directly
    verify_langsmith_traces()