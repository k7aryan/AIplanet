# app/schemas.py
from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    document_id: int
    filename: str
    text_length: int

class QuestionResponse(BaseModel):
    question: str
    answer: str

class DocumentCreate(BaseModel):
    filename: str
    content: str  # Or any other fields you need for creating a document
