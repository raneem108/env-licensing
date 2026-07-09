


from fastapi import APIRouter
from schemas.query import QueryRequest, QueryResponse
from ai.rag import search_documents, generate_answer
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

router = APIRouter()

@router.post("/query/")
def query_documents(request: QueryRequest):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(
        collection_name="regulations",
        embedding_function=embeddings,
        persist_directory="data/vectors"
    )
    
    # 1. Search for chunks
    chunks = search_documents(request.question, vectorstore)
    
    # 2. Generate answer from chunks using LLM
    answer = generate_answer(request.question, chunks)
    
    # 3. Get sources
    sources = [doc.metadata.get("source", "Unknown") for doc in chunks]
    
    return QueryResponse(answer=answer, sources=sources)