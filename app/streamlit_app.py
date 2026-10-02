import streamlit as st
from pathlib import Path

from generation.rag_chain import create_rag_chain


# Page configuration
st.set_page_config(
    page_title="ICICI Loan RAG",
    page_icon="🏦",
    layout="centered"
)


# Title
st.title("🏦 ICICI Bank Loan Assistant")
st.caption("Ask questions about ICICI Bank loan terms and conditions.")


# Create RAG chain once
@st.cache_resource
def load_rag():
    return create_rag_chain()


rag = load_rag()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input(
    "Ask about ICICI loan terms..."
)


if question:

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching ICICI loan documents..."):

            answer, sources = rag(question)

        st.markdown(answer)


        # Sources
        if sources:

            st.markdown("### 📚 Sources")

            for source in sources:

                filename = Path(
                    source["source"]
                ).name

                page = source["page"]

                st.markdown(
                    f"- **{filename}** — Page {page}"
                )


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )