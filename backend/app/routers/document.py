# app/routers/document.py
import os
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import DocumentUploadResponse
from app.crud import create_document
from app.services.pdf_processing import extract_text_from_pdf
from app.config import UPLOAD_FOLDER

router = APIRouter()

@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    document = create_document(db, filename=file.filename)
    
    return DocumentUploadResponse(document_id=document.id, filename=document.filename, text_length=len(text))
