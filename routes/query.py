

from fastapi import APIRouter
from schemas.query import QueryRequest, QueryResponse
from ai.rag import search_documents
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
    results = search_documents(request.question, vectorstore)
    answer = " ".join([doc.page_content for doc in results])
    sources = [doc.metadata.get("source", "Unknown") for doc in results]
    return QueryResponse(answer=answer, sources=sources)