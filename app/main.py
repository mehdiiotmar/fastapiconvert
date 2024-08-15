from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from pdf2image import convert_from_path
from PIL import Image
import fitz  
from .services.convert_services  import convert_pdf_to_text_service
from .services.convert_services  import convert_image_to_pdf_service
from .services.convert_services  import convert_pdf_to_image_service

app = FastAPI()

@app.post("/convert/pdf-to-text/")
async def convert_pdf_to_text(file: UploadFile = File(...)):
    return await convert_pdf_to_text_service(file)

@app.post("/convert/image-to-pdf/")
async def convert_image_to_pdf(file: UploadFile = File(...)):
    return await convert_image_to_pdf_service(file)

@app.post("/convert/pdf-to-image/")
async def convert_pdf_to_image(file: UploadFile = File(...)):
    return await convert_pdf_to_image_service(file)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de conversion de fichiers. Utilisez POST /convert/pdf-to-text, /convert/image-to-pdf, ou /convert/pdf-to-image pour convertir des fichiers."}
