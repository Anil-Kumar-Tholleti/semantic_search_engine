import os
from utils.pdf_parser import extract_text_from_pdf, chunk_text
from utils.embedding_generator import EmbeddingGenerator
from utils.search_engine import SemanticSearchEngine

def load_pdfs(pdf_dir):
    all_chunks = []
    all_files = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            print(f"📄 Processing {file}...")
            text = extract_text_from_pdf(path)
            chunks = chunk_text(text)
            all_chunks.append((file, chunks))
    return all_chunks

def main():
    pdf_dir = "pdfs"  # Folder where you put input PDFs
    query = input("🔍 Enter your search query: ")

    print("📖 Loading and processing PDFs...")
    all_chunks = load_pdfs(pdf_dir)

    print("🧠 Generating embeddings...")
    embedder = EmbeddingGenerator()
    search_engine = SemanticSearchEngine(dimension=384)  # 384 for all-MiniLM-L6-v2

    for file_name, chunks in all_chunks:
        embeddings = embedder.generate(chunks)
        search_engine.add(embeddings, chunks, file_name)

    print("🔎 Searching FAISS index...")
    query_embedding = embedder.generate([query])[0]
    results = search_engine.search(query_embedding, top_k=5)

    print("\n📌 Top Results:")
    for i, res in enumerate(results, 1):
        print(f"\n🔹 Result {i}")
        print(f"📄 File: {res['file']}")
        print(f"🧾 Text: {res['text'][:300]}...")
        print(f"📊 Similarity Score (lower = more similar): {res['score']:.4f}")

if __name__ == "__main__":
    main()
