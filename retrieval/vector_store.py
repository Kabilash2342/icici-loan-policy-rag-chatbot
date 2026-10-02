from pathlib import Path

import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from ingestion.document_loader import load_documents
from ingestion.text_splitter import split_documents


CHROMA_DIR = Path("vector_db/chroma_db")
COLLECTION_NAME = "icici_loan_documents"


def create_vector_store():

    # Load PDFs
    documents = load_documents()

    # Split into chunks
    chunks = split_documents(documents)

    print(f"Creating embeddings for {len(chunks)} chunks...")

    # Embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create Chroma vector store
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name=COLLECTION_NAME
    )

    print("Vector store created successfully!")

    return vector_store


if __name__ == "__main__":
    create_vector_store()