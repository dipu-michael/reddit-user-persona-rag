from dotenv import load_dotenv
from reddit_scraper import scrape_user
from chunker import load_user_data, chunk_text
from embedder import embed_chunks
from persona_generator import generate_persona



load_dotenv()


username = "kojied"  


scrape_user(username)

data = load_user_data(username)

chunks = chunk_text(data)

embed_chunks(chunks)


generate_persona("faiss_index", username)
