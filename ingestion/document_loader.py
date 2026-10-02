from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


DATA_DIR = Path("data/raw")


def load_documents():
    documents = []

    for pdf_file in DATA_DIR.glob("*.pdf"):
        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()

        documents.extend(docs)

    print(f"\nTotal pages loaded: {len(documents)}")

    return documents


if __name__ == "__main__":
    documents = load_documents()

    for doc in documents[:3]:
        print("\n--- Document ---")
        print(doc.page_content[:500])
        print("Metadata:", doc.metadata)