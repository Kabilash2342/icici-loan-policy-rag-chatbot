from document_loader import load_documents
from text_splitter import split_documents


documents = load_documents()

chunks = split_documents(documents)

print("\nFirst chunk:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)