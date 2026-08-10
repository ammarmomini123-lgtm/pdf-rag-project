import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Directories
    RAW_DATA_DIR = "data/raw"
    VECTOR_DB_DIR = "data/vector_db"

    # Ingestion Parameters
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 150

    # Models
    EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
    LLM_MODEL_NAME = "llama-3.1-8b-instant"
    TOP_K = 4

settings = Settings()