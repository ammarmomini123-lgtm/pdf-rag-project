# 📚 Enterprise PDF RAG Assistant

A modular Retrieval-Augmented Generation (RAG) system built with **LangChain**, **Groq (Llama-3.1-8B)**, **ChromaDB**, **SentenceTransformers**, and **Streamlit**. 

This application automatically processes PDF documents, indexes text chunks into a persistent vector store, and provides precise, document-grounded answers to user questions using a clean, layered pipeline design.

---

## 🏗️ Project Architecture

The repository enforces a clean separation of concerns without coupling frontend, logic, or storage layers:

```text
rag-project/
│
├── app/
│   ├── config/
│   │   ├── settings.py         # System parameters, models, & paths
│   │   └── prompts.py          # Grounded RAG prompt templates
│   │
│   ├── loaders/
│   │   └── pdf_loader.py       # PDF file & directory ingestion
│   │
│   ├── chunking/
│   │   └── chunker.py          # Document splitting logic
│   │
│   ├── embeddings/
│   │   └── embedding_model.py  # Local vector embedding generation
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py     # ChromaDB persistence & similarity search
│   │
│   ├── retriever/
│   │   └── retriever.py        # Context retrieval interface
│   │
│   ├── llm/
│   │   └── llm.py              # Groq LLM client setup
│   │
│   └── pipelines/
│       ├── ingestion_pipeline.py # Orchestrates load -> chunk -> embed -> store
│       ├── retrieval_pipeline.py # Orchestrates search & context extraction
│       └── rag_pipeline.py       # Combines retrieval with LLM answer generation
│
├── data/
│   ├── raw/                    # Stores uploaded source PDFs
│   ├── processed/              # Processed file cache
│   └── vector_db/              # Persistent ChromaDB vector database
│
├── streamlit_app.py            # Streamlit web application interface
├── main.py                     # CLI entry point for local pipeline testing
├── requirements.txt            # Environment dependencies
├── .env                        # Local environment variables (API keys)
└── .gitignore                  # Git untracked pattern rule
```text
```

## 🚀 Key Features
Modular Pipeline Architecture: Pure single-responsibility Python modules separated into config, loaders, chunkers, embeddings, storage, and orchestration pipelines.

Automatic PDF Discovery: Ingestion pipeline scans directory paths and ingests new .pdf documents dynamically.

Persistent Vector Store: Utilizes ChromaDB on local disk storage to avoid re-embedding unchanged documents.

Strict Context Grounding: System prompts explicitly force the LLM to restrict answers to retrieved document context.

Streamlit Web Interface: Features file upload, document re-indexing, interactive chat, and expandable source preview with similarity score tracking.

## 🛠️ Tech Stack
Framework: Python 3.12+ / LangChain

LLM Provider: Groq API (llama-3.1-8b-instant)

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Vector Database: ChromaDB

UI: Streamlit

## ⚡ Quickstart & Installation
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_USERNAME/pdf-rag-project.git](https://github.com/YOUR_USERNAME/pdf-rag-project.git)
cd pdf-rag-project
2. Set Up Virtual Environment
Using standard venv or uv:

Bash
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root directory and add your Groq API key:

Code snippet
GROQ_API_KEY=your_actual_groq_api_key_here

##🖥️ Usage Guide
Running the Web Interface (Streamlit)
Launch the web UI locally:

Bash
streamlit run streamlit_app.py
Upload your PDF document in the sidebar.

Click Process & Ingest Documents.

Ask questions in the main input field and review the generated response alongside source citation details.

Running via Terminal (CLI)
Place a target PDF in data/raw/ and execute main.py:

Bash
python main.py
## ☁️ Deployment (Streamlit Cloud)
Push this repository to GitHub (ensure .env is omitted via .gitignore).

Log in to Streamlit Community Cloud.

Connect your repository and set the Main file path to streamlit_app.py.

Add your API key in Advanced Settings -> Secrets:

Ini, TOML
GROQ_API_KEY = "your_actual_groq_api_key_here"
Click Deploy!