# 🤖 Task 5 — AI-Powered Document RAG Chatbot Dashboard
### Practical Evaluation Project | AI Internship Program — DevSynt

A full-stack, enterprise-grade Retrieval-Augmented Generation (RAG) application featuring an interactive 3-tab Streamlit dashboard, a FastAPI backend API, multi-format document processing (PDF, DOCX, TXT), persistent ChromaDB vector storage, and strict citation grounding powered by Google Gemini.

---

## 🌐 Project Deliverables & Submission Links

* **Live Dashboard UI:** [https://your-app.streamlit.app](https://your-app.streamlit.app) *(or your Vercel link)*
* **Loom Video Demo (3–5 min):** [https://www.loom.com/share/your-loom-video-id](https://www.loom.com/share/your-loom-video-id)
* **LinkedIn Post:** [Link to your LinkedIn submission post tagging DevSynt](https://www.linkedin.com)


---

## 🏗️ System Architecture & Data Flow

```text
DOCUMENT INGESTION SIDE
Upload (PDF / DOCX / TXT)
        ↓
Text Extraction & Metadata Tagging (doc_id, page_num, file_type)
        ↓
Recursive Character Chunking (chunk_size: 700, overlap: 100)
        ↓
Vector Embeddings (sentence-transformers / all-MiniLM-L6-v2)
        ↓
ChromaDB Persistent Vector Store

QUESTION & ANSWER SIDE
User Question Input
        ↓
Query Embedding & Cosine Similarity Search
        ↓
Top-K Context Retrieval + Min Score Threshold Filter
        ↓
Strict System Prompt Grounding (Gemini 1.5 Flash)
        ↓
Grounded Answer + Source References (📄 File — Page X)
        ↓
Streamlit Dashboard / FastAPI Response
```
## 📂 Repository Structure

rag-project/

│
├── app/
│   ├── config/
│   │   ├── settings.py         # App configuration, env variables, & model parameters
│   │   └── prompts.py          # Grounded RAG system instructions & citation prompts
│   │
│   ├── loaders/
│   │   └── document_loader.py  # Multi-format parser (PDF, DOCX, TXT) with metadata extraction
│   │
│   ├── chunking/
│   │   └── chunker.py          # Recursive text splitting & chunk ID assignment
│   │
│   ├── embeddings/
│   │   └── embedding_model.py  # SentenceTransformers wrapper for vector generation
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py     # Persistent ChromaDB client, stats, & deletion operations
│   │
│   ├── retriever/
│   │   └── retriever.py        # Semantic search & score filtering interface
│   │
│   ├── llm/
│   │   └── llm.py              # Google Gemini API client provider
│   │
│   └── pipelines/
│       ├── ingestion_pipeline.py # Orchestrates load -> chunk -> embed -> store
│       ├── retrieval_pipeline.py # Standalone semantic search & context extractor
│       └── rag_pipeline.py       # Combines context retrieval with Gemini answer generation
│
├── data/
│   └── raw/                    # Stores uploaded real-estate sample documents
│
├── generate_sample_pdfs.py     # Script to generate the 5 synthetic real-estate test PDFs
├── main.py                     # FastAPI REST API Backend & CLI entry point
├── streamlit_app.py            # 3-Tab Streamlit Dashboard UI
├── requirements.txt            # System dependencies
├── .env                        # Local environment keys (API keys)
└── .gitignore                  # Git untracked pattern rules

## 🚀 Key Features

3-Tab Dashboard UI: Includes real-time KPI metrics cards, document ingestion management with file deletion, and a multi-turn chat interface.

Multi-Format Ingestion: Extracts text and attaches page/document metadata across .pdf, .docx, and .txt files.

Persistent Vector Storage: Leverages ChromaDB on disk to prevent redundant embedding computation.

Strict Anti-Hallucination Guardrails: Enforces strict context grounding. If data does not exist in uploaded files, the model explicitly responds: "The requested information could not be found in the uploaded documents."

Granular Source Citations: Every valid response displays expandable source blocks containing document names, page numbers, relevance scores, and text snippets (📄 Document_Name.pdf — Page X).

## 🛠️ Tech Stack
Programming Language: Python 3.12+

LLM Engine: Google Gemini 1.5 Flash / Gemini 2.5 Flash

Embedding Model: sentence-transformers/all-MiniLM-L6-v2

Vector Database: ChromaDB

Backend API: FastAPI / Uvicorn

Frontend Interface: Streamlit

Document Processing: pypdf, Python standard libraries

## ⚡ Quickstart & Installation

1. Clone Repository & Setup Environment
Bash
git clone [https://github.com/YOUR_USERNAME/rag-project.git](https://github.com/YOUR_USERNAME/rag-project.git)
cd rag-project

python -m venv .venv
# Activate on Windows:
.\.venv\Scripts\activate
# Activate on macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
2. Configure Environment Variables
Create a .env file in the root folder:

Ini, TOML
GEMINI_API_KEY=your_google_gemini_api_key_here
RAW_DATA_DIR=data/raw
VECTOR_DB_DIR=data/vector_db
CHUNK_SIZE=700
CHUNK_OVERLAP=100
TOP_K=4
3. Generate Sample Real-Estate PDFs
Generate the 5 synthetic test documents for AeroEstate Realty:

Bash
python generate_sample_pdfs.py

## 🖥️ Running the Application
Option A: Running the Full Stack (Backend API + Frontend UI)
Terminal 1 — Launch FastAPI Backend:

Bash
python main.py
API interactive docs available at: http://localhost:8000/docs

Terminal 2 — Launch Streamlit Dashboard:

Bash
streamlit run streamlit_app.py
Access UI at: http://localhost:8501

## 📊 Evaluation & Test Matrix (10 Scenario Report)
The system was evaluated against the 5 generated AeroEstate Realty documents (Company_Overview.pdf, Property_Listings.pdf, Services_and_Fees.pdf, Frequently_Asked_Questions.pdf, Terms_and_Policies.pdf)
Test ID,Query Scenario,Question Asked,Expected Behavior / Grounded Citation,Result
Q1,Direct Fact Lookup,What is the seller commission fee at AeroEstate Realty?,Returns 2.5% fee citing Services_and_Fees.pdf — Page 1,PASS
Q2,Specific Listing Query,What are the specs and price of Skyline Heights Penthouse?,"Returns $350,000, 3 Bed/4 Bath citing Property_Listings.pdf — Page 1",PASS
Q3,Policy Verification,What is the escrow deposit policy for buyer token money?,Returns 5% minimum deposit rule citing Terms_and_Policies.pdf — Page 1,PASS
Q4,Multi-Document Synthesis,Compare property management fee with landlord cancellation rules.,Synthesizes 8% fee (Services.pdf) & 30-day email notice (FAQ.pdf),PASS
Q5,Executive Team Query,Who is the CEO of AeroEstate Realty and what is her background?,Returns Sarah Jenkins citing Company_Overview.pdf — Page 2,PASS
Q6,Commercial Lease Lookup,What are the lease terms for the Blue Area commercial office?,"Returns $4,500/month, Floor 7 citing Property_Listings.pdf — Page 2",PASS
Q7,FAQ Lookup,Can overseas Pakistanis purchase properties remotely?,Returns Yes via NICOP/POA citing Frequently_Asked_Questions.pdf — Page 1,PASS
Q8,Hallucination Test,Does AeroEstate allow payment using Bitcoin or Ethereum?,Refuses answer; states info could not be found in documents,PASS
Q9,Out-of-Domain Test,What is the capital city of Australia and its population?,Refuses answer; states info could not be found in documents,PASS
Q10,Comprehensive Overview,List all legal title search and appraisal service costs.,Summarizes $500 title search & $300/$750 appraisals (Services.pdf),PASS

## 🔐 Security & Best Practices
API Keys: Kept strictly inside .env (excluded from git tracking via .gitignore).

Zero Cost Architecture: Uses open-source local embeddings (sentence-transformers) and free-tier Gemini API access.