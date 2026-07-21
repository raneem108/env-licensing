from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.document import Document
from ai.rag import process_document
import shutil
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/documents/upload/")
async def upload_document(
    file: UploadFile = File(...),
    title: str = Form(...),
    description: str = Form(None),
    db: Session = Depends(get_db)
):
    # Save file to disk
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Save record to database
    doc = Document(
        title=title,
        doc_type=file.content_type,
        file_path=file_path,
        description=description,
        size=os.path.getsize(file_path),
        created_at=datetime.now()
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    
    # Process with RAG
    process_document(file_path, collection_name=f"doc_{doc.id}")
    
    return {
        "message": "Document uploaded and processed successfully",
        "document_id": doc.id,
        "title": title,
        "file_path": file_path
    }