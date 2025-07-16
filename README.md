# 🤖 Reddit User Persona Generator (RAG-based + Local Embeddings)

This project generates a detailed persona of any Reddit user based on their public comments and posts — using Retrieval-Augmented Generation (RAG) with **local embeddings (sentence-transformers)** and **FAISS vector search**. No API keys or paid services required.

---

## 🚀 Features

- ✅ Scrapes Reddit posts & comments from any user
- ✅ Cleans and chunks text content
- ✅ Embeds chunks locally using `all-MiniLM-L6-v2`
- ✅ Stores embeddings in a FAISS vector database
- ✅ Performs local vector similarity search
- ✅ Synthesizes a user persona using top relevant posts
- ✅ Outputs insights with links to original Reddit content
- ✅ 100% offline — no OpenAI key or internet needed after scraping

---

## 📦 Technologies Used

| Tool | Purpose |
|------|---------|
| `praw` | Reddit API scraper |
| `sentence-transformers` | Local text embeddings |
| `faiss-cpu` | Fast vector similarity search |
| `tqdm` | Progress tracking |
| `pickle` | Metadata persistence |
| `scikit-learn` | (optional) cosine similarity |

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/reddit-user-persona-rag.git
cd reddit-user-persona-rag
