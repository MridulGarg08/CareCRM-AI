import chromadb

_client = chromadb.PersistentClient(path="./chroma_data")

_collection = _client.get_or_create_collection(name="knowledge_base")


def add_chunks(chunks: list[str], embeddings: list[list[float]], source: str):
    ids = [f"{source}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source, "chunk_index": i} for i in range(len(chunks))]

    _collection.add(
        ids=ids,
        # pyrefly: ignore [bad-argument-type]
        embeddings=embeddings,
        documents=chunks,
        # pyrefly: ignore [bad-argument-type]
        metadatas=metadatas,
    )


def search(query_embedding: list[float], top_k: int = 3):
    results = _collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )
    return results