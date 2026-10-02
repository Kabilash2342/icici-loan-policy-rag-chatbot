from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


CHROMA_DIR = "vector_db/chroma_db"
COLLECTION_NAME = "icici_loan_documents"


def get_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    return vector_store


def retrieve_documents(question, k=4):

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(
        question,
        k=k
    )

    return results