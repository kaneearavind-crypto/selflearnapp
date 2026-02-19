import chromadb
from uuid import uuid4

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="vectorstore"
    )
)

collection = client.get_or_create_collection(
    name="selflearn",
    embedding_function=chromadb.utils.embedding_functions.OllamaEmbeddingFunction(
        model_name="mxbai-embed-large"
    )
)

def add_texts_to_vectorstore(texts, source_name):
    ids = [str(uuid4()) for _ in texts]
    metadatas = [{"source": source_name} for _ in texts]

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

def get_sources():
    data = collection.get()
    if not data["metadatas"]:
        return []
    return sorted(list(set(m["source"] for m in data["metadatas"])))
