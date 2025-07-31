import faiss
import numpy as np

class SemanticSearchEngine:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []
        self.files = []

    def add(self, embeddings, texts, file_name):
        self.index.add(np.array(embeddings, dtype=np.float32))
        self.texts.extend(texts)
        self.files.extend([file_name] * len(texts))

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        results = []
        for idx, score in zip(I[0], D[0]):
            if idx < len(self.texts):
                results.append({
                    'file': self.files[idx],
                    'text': self.texts[idx],
                    'score': score
                })
        return results
