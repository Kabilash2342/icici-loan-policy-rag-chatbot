from generation.rag_chain import create_rag_chain
from pathlib import Path

rag = create_rag_chain()

question = "What happens if the borrower fails to pay the loan installment?"

answer, sources = rag(question)


print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(answer)


print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for source in sources:

    print(
    f"{Path(source['source']).name} - "
    f"Page {source['page']}"
)