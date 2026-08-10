from typing import Dict, Any
from app.pipelines.retrieval_pipeline import RetrievalPipeline
from app.llm.llm import LLMProvider
from app.config.prompts import RAG_PROMPT_TEMPLATE

class RAGPipeline:
    """Combines context retrieval with LLM generation."""

    def __init__(self):
        self.retrieval_pipeline = RetrievalPipeline()
        self.llm = LLMProvider().get_llm()
        self.prompt = RAG_PROMPT_TEMPLATE

    def run(self, question: str) -> Dict[str, Any]:
        retrieved_chunks = self.retrieval_pipeline.run(question)

        if not retrieved_chunks:
            return {
                "answer": "No relevant context found in the database.",
                "context": []
            }

        context_str = "\n\n---\n\n".join([
            f"Source: {chunk['source']} (Page {chunk['page'] + 1})\nContent: {chunk['content']}"
            for chunk in retrieved_chunks
        ])

        chain = self.prompt | self.llm
        response = chain.invoke({"context": context_str, "question": question})

        return {
            "answer": response.content,
            "context": retrieved_chunks
        }