from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str) -> list[float]:
    embedding = _model.encode(text)
    return embedding.tolist()


def embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = _model.encode(texts)
    return embeddings.tolist()