import os
import pypdf
import chromadb

DATA_DIR = "data"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "course_materials"

MAX_CHARS = 1200
OVERLAP = 150


def chunk_text(text: str, max_chars: int = MAX_CHARS, overlap: int = OVERLAP) -> list[str]:
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []

    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunks.append(text[start:end].strip())
        start = end - overlap
    return [c for c in chunks if c]


def load_pdf_chunks(pdf_path: str) -> list[dict]:
    reader = pypdf.PdfReader(pdf_path)
    filename = os.path.basename(pdf_path)
    chunks = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text or not text.strip():
            continue
        for piece in chunk_text(text):
            chunks.append({"text": piece, "source": filename, "page": page_number})
    return chunks


def main():
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    all_chunks = []
    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith(".pdf"):
            all_chunks.extend(load_pdf_chunks(os.path.join(DATA_DIR, filename)))

    if not all_chunks:
        print("No PDF files found in data/.")
        return

    documents = [c["text"] for c in all_chunks]
    metadatas = [{"source": c["source"], "page": c["page"]} for c in all_chunks]
    ids = [f"{c['source']}-p{c['page']}-{i}" for i, c in enumerate(all_chunks)]

    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"Stored {len(all_chunks)} chunks -> {CHROMA_DIR}/ (collection: {COLLECTION_NAME})")


if __name__ == "__main__":
    main()
