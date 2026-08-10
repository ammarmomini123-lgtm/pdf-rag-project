import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

class PDFLoader:
    """Loads PDF documents from disk."""

    def load(self, file_path: str) -> List[Document]:
        """Loads a single PDF file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        print(f"✓ Loaded {len(documents)} pages from '{file_path}'.")
        return documents

    def load_directory(self, folder_path: str) -> List[Document]:
        """Automatically scans a directory and loads all PDF files found."""
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Directory not found: {folder_path}")

        pdf_files = [
            os.path.join(folder_path, f) 
            for f in os.listdir(folder_path) 
            if f.lower().endswith(".pdf")
        ]

        if not pdf_files:
            print(f"⚠️ No PDF files found in '{folder_path}'.")
            return []

        all_documents = []
        for pdf_path in pdf_files:
            print(f"Processing detected file: {pdf_path}")
            docs = self.load(pdf_path)
            all_documents.extend(docs)

        return all_documents