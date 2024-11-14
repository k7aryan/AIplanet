import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    document = fitz.open(file_path)
    text = ""
    for page in document:
        text += page.get_text("text")  # Extracting text from each page
    return text

