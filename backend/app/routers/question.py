# app/routers/question.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import QuestionResponse
from app.crud import get_document
from app.services.nlp_processing import answer_question

router = APIRouter()

@router.post("/{document_id}/ask", response_model=QuestionResponse)
def ask_question(document_id: int, question: str, db: Session = Depends(get_db)):
    document = get_document(db, document_id)
    if not document:
        return {"error": "Document not found"}
    
    # Placeholder text extraction from document. Add retrieval here.
    document_text = "Extracted text from the document"
    
    answer = answer_question(document_text, question)
    return QuestionResponse(question=question, answer=answer)
