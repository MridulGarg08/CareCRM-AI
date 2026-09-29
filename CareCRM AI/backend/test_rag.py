from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts, embed_text
from app.rag.vector_store import add_chunks, search

text = open("../data/documents/refund_policy.txt").read()
chunks = chunk_text(text, chunk_size=30, overlap=5)

embeddings = embed_texts(chunks)

add_chunks(chunks, embeddings, source="refund_policy")

print(f"Stored {len(chunks)} chunks.\n")

query = "why is my refund taking so long?"
query_embedding = embed_text(query)

results = search(query_embedding, top_k=2)

print(f"Query: {query}\n")
for doc, metadata, distance in zip(
    # pyrefly: ignore [unsupported-operation]
    results["documents"][0], results["metadatas"][0], results["distances"][0]
):
    # pyrefly: ignore [bad-indentation]
    print(f"Source: {metadata['source']} (chunk {metadata['chunk_index']}, distance {distance:.4f})")
    # pyrefly: ignore [bad-indentation]
    print(doc)
    print()