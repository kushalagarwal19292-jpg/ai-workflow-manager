from typing import List, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# NOTE: Ensure OPENAI_API_KEY is set in your environment or config.py

def chunk_documents(documents: List[str], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """Chunks a list of documents into smaller pieces."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.create_documents([doc for doc in documents])
    return [chunk.page_content for chunk in chunks]

def create_vector_store(documents: List[str], collection_name: str = "rag_collection") -> Chroma:
    """Creates an in-memory Chroma vector store with OpenAI embeddings."""
    # Ensure OpenAIEmbeddings is configured correctly (e.g., OPENAI_API_KEY is set)
    embeddings = OpenAIEmbeddings()
    
    # Chunk documents before creating vector store
    chunked_documents = chunk_documents(documents)
    
    # Using .from_documents to create the vector store with embeddings
    vector_store = Chroma.from_texts(texts=chunked_documents, embedding=embeddings, collection_name=collection_name)
    return vector_store

def retrieve_documents(vector_store: Chroma, query: str, k: int = 5) -> List[str]:
    """Retrieves top k relevant documents from the vector store based on a query."""
    docs = vector_store.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]

print(f"Created {project_root}/utils/rag_utils.py")
