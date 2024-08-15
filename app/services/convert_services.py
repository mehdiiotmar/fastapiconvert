from fastapi import UploadFile, HTTPException
from io import BytesIO
from pdf2image import convert_from_path
from PIL import Image
import fitz  # PyMuPDF
from fastapi.responses import StreamingResponse

async def convert_pdf_to_text_service(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être au format PDF")

    pdf_file = BytesIO(await file.read())
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    return {"text": text}

async def convert_image_to_pdf_service(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Le fichier doit être une image JPEG ou PNG")

    image_file = BytesIO(await file.read())
    image = Image.open(image_file)

    pdf_bytes = BytesIO()
    image.save(pdf_bytes, format="PDF")
    pdf_bytes.seek(0)

    return StreamingResponse(pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=output.pdf"})

async def convert_pdf_to_image_service(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être au format PDF")

    pdf_file = BytesIO(await file.read())
    images = convert_from_path(pdf_file)

    image_bytes = BytesIO()
    images[0].save(image_bytes, format="PNG")
    image_bytes.seek(0)

    return StreamingResponse(image_bytes, media_type="image/png", headers={"Content-Disposition": "attachment; filename=output.png"})
