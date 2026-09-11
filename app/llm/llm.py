import os
from typing import Optional
from langchain_groq import ChatGroq
from app.config.settings import settings


class LLMProvider:
    """Initializes and exposes the Groq LLM instance."""

    def __init__(
        self, 
        model_name: Optional[str] = None, 
        temperature: float = 0.0
    ):
        # Retrieve API key
        api_key = getattr(settings, "GROQ_API_KEY", None) or os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing from settings or environment variables."
            )

        # Default model selection: llama-3.3-70b-versatile
        selected_model = (
            model_name 
            or getattr(settings, "LLM_MODEL_NAME", None) 
            or "llama-3.3-70b-versatile"
        )

        print(f"⚡ Initializing ChatGroq with model: '{selected_model}'")

        self.llm = ChatGroq(
            model=selected_model,
            groq_api_key=api_key,
            temperature=temperature,
            max_tokens=1024,
        )

    def get_llm(self) -> ChatGroq:
        """Returns the configured ChatGroq instance."""
        return self.llm


# Backward-compatibility alias
LLMClient = LLMProvider