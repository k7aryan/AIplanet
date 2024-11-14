# app/main.py
from fastapi import FastAPI
from app.routers import document, question
from app.database import Base, engine
from app.crud import create_document
from app.schemas import DocumentCreate
from app.services.pdf_processing import extract_text_from_pdf
from app.crud import get_document
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload
# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI instance
app = FastAPI()

# Include routers
app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(question.router, prefix="/questions", tags=["Questions"])

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF Q&A API"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload.router, prefix="/api") 