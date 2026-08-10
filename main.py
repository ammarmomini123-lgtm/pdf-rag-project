import os
from app.pipelines.ingestion_pipeline import IngestionPipeline
from app.pipelines.rag_pipeline import RAGPipeline
from app.config.settings import settings

def main():
    # Set the folder path
    raw_dir = settings.RAW_DATA_DIR

    # 1. Run Ingestion Pipeline (automatically picks up any .pdf in data/raw/)
    ingestion = IngestionPipeline()
    ingestion.run(raw_dir)

    # 2. Run RAG Pipeline
    rag = RAGPipeline()
    query = "What is the maximum timeframe within which Cogen must publish its annual accounts?"
    
    print(f"\n❓ Question: {query}")
    result = rag.run(query)

    print("\n💡 Answer:")
    print(result["answer"])

    print("\n📚 Retrieved Sources:")
    for idx, chunk in enumerate(result["context"], 1):
        print(f"[{idx}] Source: {chunk['source']} | Page {chunk['page'] + 1} (Score: {chunk['score']:.4f})")

if __name__ == "__main__":
    main()