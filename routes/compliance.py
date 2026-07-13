from fastapi import APIRouter
from pydantic import BaseModel
from ai.compliance import check_compliance

router = APIRouter()

class ComplianceRequest(BaseModel):
    activity_type: str
    distance: int

@router.post("/compliance/check/")
def compliance_check(request: ComplianceRequest):
    result = check_compliance(request.activity_type, request.distance)
    return result

from ai.rag import search_documents, generate_answer
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from schemas.compliance import CombinedRequest, CombinedResponse

@router.post("/compliance/analyze/")
def analyze_project(request: CombinedRequest):
    # Step 1 — Check compliance
    compliance_result = check_compliance(request.activity_type, request.distance)
    
    # Step 2 — Load vectorstore
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(
        collection_name="regulations",
        embedding_function=embeddings,
        persist_directory="data/vectors"
    )
    
    # Step 3 — RAG query
    chunks = search_documents(request.question, vectorstore)
    regulation_answer = generate_answer(request.question, chunks)
    sources = [doc.metadata.get("source", "Unknown") for doc in chunks]
    
    # Step 4 — Combined response
    return CombinedResponse(
        activity_type=request.activity_type,
        category=compliance_result.get("category", "Unknown"),
        approved=compliance_result.get("approved", False),
        required_distance=compliance_result.get("required_distance", 0),
        provided_distance=request.distance,
        reason=compliance_result.get("reason", ""),
        regulation_answer=regulation_answer,
        sources=sources
    ) 