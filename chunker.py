import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_user_data(username):
    with open(f"data/{username}.json", "r") as f:
        return json.load(f)

def chunk_text(data, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = []

    for item in data:
        split_texts = splitter.split_text(item["text"])
        for text in split_texts:
            chunks.append({
                "text": text,
                "url": item["url"]
            })
    return chunks
