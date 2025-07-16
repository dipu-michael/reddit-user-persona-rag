import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_persona(faiss_path, username, query="Generate a user persona from this content."):
    print("📂 Loading index and metadata...")
    index = faiss.read_index(os.path.join(faiss_path, "index.faiss"))
    with open(os.path.join(faiss_path, "metadata.pkl"), "rb") as f:
        texts, urls = pickle.load(f)

    print("🔍 Searching most relevant chunks...")
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, 5)

    relevant_chunks = [texts[i] for i in I[0]]
    relevant_sources = [urls[i] for i in I[0]]

    print("🧠 Synthesizing offline persona...")
    output = f"🧑 Reddit User Persona for {username}\n\n"
    for i, (chunk, url) in enumerate(zip(relevant_chunks, relevant_sources), 1):
        output += f"### Insight {i}:\n"
        output += f"{chunk.strip()}\n🔗 Source: {url}\n\n"

    output_path = f"output/{username}_persona.txt"
    os.makedirs("output", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(output)

    print(f"✅ Persona written to {output_path}")
