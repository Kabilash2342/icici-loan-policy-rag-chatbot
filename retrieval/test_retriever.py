from retrieval.retriever import retrieve_documents


question = "What happens if the borrower fails to pay the loan installment?"

results = retrieve_documents(question, k=4)


print(f"\nRetrieved {len(results)} documents\n")


for i, (doc, score) in enumerate(results, start=1):

    print("=" * 60)
    print(f"RESULT {i}")
    print("=" * 60)

    print(f"\nSimilarity distance: {score}")

    print("\nContent:")
    print(doc.page_content)

    print("\nSource:")
    print(doc.metadata.get("source"))

    print("Page:")
    print(doc.metadata.get("page"))