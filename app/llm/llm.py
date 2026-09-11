import os
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config.settings import settings


class LLMProvider:
    """Initializes and exposes the Google Gemini LLM instance."""

    def __init__(
        self, 
        model_name: Optional[str] = None, 
        temperature: float = 0.0
    ):
        # Retrieve API key checking GEMINI_API_KEY first, then GOOGLE_API_KEY fallback
        api_key = getattr(settings, "GEMINI_API_KEY", None) or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError(
                "Neither GEMINI_API_KEY nor GOOGLE_API_KEY is configured in settings or environment."
            )

        # Default model selection with fallback
        raw_model_name = (
            model_name 
            or getattr(settings, "LLM_MODEL_NAME", None) 
            or "gemini-1.5-flash"
        )

        # Clean model string: strip accidental 'models/' prefix and leading/trailing whitespace
        clean_model_name = raw_model_name.replace("models/", "").strip()

        print(f"🤖 Initializing ChatGoogleGenerativeAI with model: '{clean_model_name}'")

        self.llm = ChatGoogleGenerativeAI(
            model=clean_model_name,
            google_api_key=api_key,
            temperature=temperature,
            max_output_tokens=1024,
            top_p=0.95
        )

    def get_llm(self) -> ChatGoogleGenerativeAI:
        """Returns the configured ChatGoogleGenerativeAI instance."""
        return self.llm


# Backward-compatibility alias in case pipelines reference LLMClient
LLMClient = LLMProvider