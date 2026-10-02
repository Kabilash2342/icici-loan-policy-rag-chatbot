````markdown
# ICICI Bank Loan Policy RAG Chatbot

A conversational Retrieval-Augmented Generation (RAG) chatbot that answers questions using publicly available ICICI Bank loan policy and terms & conditions documents.

The system retrieves relevant information from the loan documents and uses an LLM to generate grounded answers with source document and page references.

> **Disclaimer:** This is an educational/portfolio project and is not an official ICICI Bank application or service. The documents used are publicly available ICICI Bank terms and conditions.

---

## Features

- PDF document ingestion
- Recursive text chunking
- Document metadata preservation
- Sentence Transformer embeddings
- ChromaDB vector database
- Semantic similarity search
- Top-k document retrieval
- Retrieval-grounded LLM generation
- Source document and page references
- Conversational Streamlit interface
- Hallucination-reduction through context-restricted prompting

---

## Documents

The chatbot currently uses six ICICI Bank loan-related documents:

- Home Loan Terms
- Personal Loan Terms
- Education Loan Terms
- Vehicle / Equipment Loan Terms
- Gold Loan Terms
- Loan Against Securities Terms

The ingestion pipeline processes the documents into **545 searchable chunks**.

---

## Architecture

```text
                ICICI Loan PDFs
                       |
                       v
                PDF Ingestion
                 PyPDFLoader
                       |
                       v
              Text Chunking
          RecursiveCharacterTextSplitter
                       |
                       v
             Sentence Transformers
                 Embeddings
                       |
                       v
                  ChromaDB
               Vector Storage
                       |
                       v
               Similarity Search
                       |
                       v
              Retrieved Documents
                       |
                       v
             Retrieval Context
                       |
                       v
                  Groq LLM
                       |
                       v
             Grounded Response
                       |
                       v
              Source + Page Info
                       |
                       v
                 Streamlit UI
```
````

---

## Project Structure

```text
ICIC rag chatbot/
│
├── app/
│   └── streamlit_app.py
│
├── config/
│   └── config.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── ingestion/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   └── test_ingestion.py
│
├── retrieval/
│   ├── __init__.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── test_retriever.py
│
├── generation/
│   ├── __init__.py
│   ├── prompt.py
│   ├── rag_chain.py
│   └── test_rag.py
│
├── evaluation/
│   ├── test_questions.json
│   └── evaluate_rag.py
│
├── vector_db/
│   └── chroma_db/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---

## Tech Stack

### Programming

- Python

### Generative AI

- Large Language Models
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Context Grounding

### AI / NLP

- Sentence Transformers
- Hugging Face

### Frameworks

- LangChain
- LangChain Community
- LangChain Chroma

### Vector Database

- ChromaDB

### LLM

- Groq

### Backend / Interface

- Streamlit

### Document Processing

- PyPDF

---

## RAG Pipeline

### 1. Document Loading

PDF documents are loaded using `PyPDFLoader`.

### 2. Text Splitting

Documents are divided into smaller overlapping chunks using:

```text
RecursiveCharacterTextSplitter
```

Configuration:

```text
Chunk size: 1000
Chunk overlap: 200
```

### 3. Embeddings

Each chunk is converted into a vector representation using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Vector Storage

The embeddings are stored in ChromaDB.

### 5. Retrieval

For each user question, the system performs semantic similarity search and retrieves the most relevant document chunks.

### 6. Generation

The retrieved chunks are provided as context to the Groq LLM.

The prompt instructs the model to:

- Use only retrieved context
- Avoid unsupported information
- Avoid hallucinating
- State when information cannot be found
- Provide relevant document and page information

### 7. User Interface

The chatbot is exposed through a Streamlit conversational interface.

---

## Example Questions

```text
What happens if I fail to pay my personal loan installment?

What happens if I default on my gold loan?

What are the conditions for an education loan?

What happens if I default on my vehicle loan?

What are the terms related to loan against securities?
```

The chatbot also provides the source document and page number for retrieved information.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kabilash2342/icici-loan-policy-rag-chatbot.git
```

Navigate to the project:

```bash
cd icici-loan-policy-rag-chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit the `.env` file to GitHub.

---

## Build the Vector Database

Run:

```bash
python -m retrieval.vector_store
```

This loads the documents, creates chunks, generates embeddings, and stores them in ChromaDB.

---

## Run the Application

Start Streamlit:

```bash
python -m streamlit run app/streamlit_app.py
```

The application will open in your browser.

---

## Testing

Test document ingestion:

```bash
python -m ingestion.test_ingestion
```

Test retrieval:

```bash
python -m retrieval.test_retriever
```

Test the RAG pipeline:

```bash
python -m generation.test_rag
```

---

## Future Improvements

- Metadata-based filtering by loan type
- Reranking retrieved documents
- Similarity score thresholding
- Context compression
- Multi-query retrieval
- RAG evaluation metrics
- Conversation memory
- Docker deployment
- Production API using FastAPI
- Improved citation and source tracking

---

## Author

**Kabilash Pagalam B**

B.Tech Computer Science and Engineering (AI & ML)

SRM Institute of Science and Technology, Chennai

GitHub: https://github.com/Kabilash2342

````

After saving it, run:

```bash
git status
````

**Don't run `git add` yet.** Send me the output of `git status`, and I'll check that you're not accidentally about to upload `.env`, `venv`, or the ChromaDB.
