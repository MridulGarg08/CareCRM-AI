from app.rag.chunking import chunk_text

text = open("../data/documents/refund_policy.txt").read()
chunks = chunk_text(text, chunk_size=30, overlap=5)

for i, c in enumerate(chunks):
    print(f"--- Chunk {i} ---")
    print(c)
    print()