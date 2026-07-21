import re


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def chunk_text(text: str, *, max_words: int = 140, overlap: int = 25) -> list[str]:
    words = clean_text(text).split()
    if not words:
        return []
    chunks: list[str] = []
    step = max(1, max_words - overlap)
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + max_words])
        if chunk:
            chunks.append(chunk)
        if start + max_words >= len(words):
            break
    return chunks
