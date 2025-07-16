from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks, save_path="faiss_index"):
    if not chunks:
        print("❌ No chunks to embed.")
        return

    texts = [chunk["text"] for chunk in chunks]
    metadata = [chunk["url"] for chunk in chunks]

    print(f"📦 Embedding {len(texts)} chunks locally...")
    embeddings = model.encode(texts)

    # Save FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    os.makedirs(save_path, exist_ok=True)
    faiss.write_index(index, os.path.join(save_path, "index.faiss"))

    # Save metadata
    with open(os.path.join(save_path, "metadata.pkl"), "wb") as f:
        pickle.dump((texts, metadata), f)

    print(f"✅ Saved FAISS index and metadata to {save_path}")
