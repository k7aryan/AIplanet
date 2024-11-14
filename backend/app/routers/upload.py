# app/routers/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_processing import extract_text_from_pdf  # Ensure this function exists and is implemented

router = APIRouter()

# @router.post("/upload")
# async def pdf_upload(file: UploadFile = File(...)):
#     try:
#         # Read the content of the uploaded file
#         content = await file.read()
        
#         # Save the file to the filesystem (in 'uploaded_pdfs' directory)
#         with open(f"uploaded_pdfs/{file.filename}", "wb") as f:
#             f.write(content)
        
#         # (Optional) Process the PDF content if needed
#         # extracted_text = extract_text_from_pdf(content)  # Uncomment if needed

#         return {"filename": file.filename, "message": "Upload successful"}
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error uploading file: {e}")

@router.post("/upload")
async def pdf_upload(file: UploadFile = File(...)):
    # (Your file handling logic here)
    return {"filename": file.filename, "message": "Upload successful"}
