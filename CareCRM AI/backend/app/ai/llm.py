# pyrefly: ignore [missing-import]
import ollama


def generate_answer(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""You are CareCRM AI, a helpful customer support assistant.
Answer the user's question using ONLY the context below. If the context doesn't contain the answer, say you don't have enough information.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )

    return response["message"]["content"]