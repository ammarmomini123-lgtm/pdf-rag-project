from langchain_groq import ChatGroq
from app.config.settings import settings

class LLMProvider:
    """Initializes and exposes the Groq LLM instance."""

    def __init__(self):
        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set in the environment or .env file.")
        
        self.llm = ChatGroq(
            groq_api_key=settings.GROQ_API_KEY,
            model_name=settings.LLM_MODEL_NAME,
            temperature=0.1
        )

    def get_llm(self):
        return self.llm