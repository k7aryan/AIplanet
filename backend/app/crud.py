from sqlalchemy.orm import Session
from app.models import Document
from app.schemas import DocumentCreate

def create_document(db: Session, document: DocumentCreate) -> Document:
    db_document = Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
def get_document(db: Session, document_id: int) -> Document:
    return db.query(Document).filter(Document.id == document_id).first()