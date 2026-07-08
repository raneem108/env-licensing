
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def process_document(pdf_path: str, collection_name: str = "regulations"):
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the document into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # Create embeddings for the document chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Store the embeddings in a Chroma vector store
    vectorstore = Chroma.from_documents(documents=chunks,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory="data/vectors")

    return vectorstore




def search_documents(query: str, vectorstore, top_k: int = 5):
    """
    Search for documents in the vectorstore based on the query.

    Args:
        query (str): The search query.
        vectorstore: The vectorstore to search in.
        top_k (int): The number of top results to return.

    Returns:
        List[Document]: A list of documents that match the query.
    """
    # Perform the search in the vectorstore
    results = vectorstore.similarity_search(query, k=top_k)
    
    # Return the list of documents
    return results