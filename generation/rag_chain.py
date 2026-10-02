from dotenv import load_dotenv
from langchain_groq import ChatGroq

from generation.prompt import RAG_PROMPT
from retrieval.retriever import retrieve_documents


load_dotenv()


def get_unique_sources(documents):

    sources = []

    for doc in documents:

        source = doc.metadata.get("source")
        page = doc.metadata.get("page")

        source_info = {
            "source": source,
            "page": page
        }

        if source_info not in sources:
            sources.append(source_info)

    return sources


def create_rag_chain():

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
    )

    def rag(question):

        # Retrieve relevant documents
        results = retrieve_documents(question, k=4)

        # Extract documents from results
        documents = [doc for doc, score in results]

        # Get unique sources
        sources = get_unique_sources(documents)

        # Build context
        context = "\n\n".join(
            [
                f"Source: {doc.metadata.get('source')}, "
                f"Page: {doc.metadata.get('page', 'Unknown')}\n"
                f"{doc.page_content}"
                for doc in documents
            ]
        )

        # Create prompt
        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question
            }
        )

        # Generate answer
        response = llm.invoke(prompt)

        return response.content, sources

    return rag