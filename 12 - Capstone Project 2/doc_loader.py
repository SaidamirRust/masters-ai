import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def load_and_index_documents(data_dir="data"):
    """Load documents from `data_dir`, split into chunks, and create a Chroma vector store."""
    docs = []
    # Load PDF and text files
    for filename in os.listdir(data_dir):
        path = os.path.join(data_dir, filename)
        if filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(path)
            pages = loader.load_and_split()  # each page has metadata with 'page' info:contentReference[oaicite:15]{index=15}
            docs.extend(pages)
        elif filename.lower().endswith(".txt"):
            loader = TextLoader(path, encoding='utf-8')
            docs.extend(loader.load())  # single Document
        # (Add other formats if needed)
    # Split documents into chunks with overlap
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    # Create embeddings and vector store (Chroma)
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store

# Example usage (called at app startup)
# vectordb = load_and_index_documents()