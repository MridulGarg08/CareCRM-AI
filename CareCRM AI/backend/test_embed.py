from app.rag.embeddings import embed_text

vec1 = embed_text("refund policy")
vec2 = embed_text("money back guarantee")
vec3 = embed_text("pizza toppings")

print("Vector length:", len(vec1))
print("First 5 values of vec1:", vec1[:5])

import numpy as np

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Similarity (refund policy vs money back guarantee):", cosine_similarity(vec1, vec2))
print("Similarity (refund policy vs pizza toppings):", cosine_similarity(vec1, vec3))