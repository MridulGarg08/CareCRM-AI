# pyrefly: ignore [missing-import]
from app.rag.embeddings import embed_text
# pyrefly: ignore [missing-import]
from app.rag.vector_store import search
# pyrefly: ignore [missing-import]
from app.ai.llm import generate_answer

query = "why is my refund taking so long?"
query_embedding = embed_text(query)

results = search(query_embedding, top_k=2)
context_chunks = results["documents"][0]

answer = generate_answer(query, context_chunks)

print("Question:", query)
print("\nRetrieved context:")
for chunk in context_chunks:
    print("-", chunk[:80], "...")

print("\nAnswer:\n", answer)