from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from search_engine import search_similar_images
import os

app = FastAPI()

# Serve dataset images
app.mount("/images", StaticFiles(directory="images"), name="images")

# Serve uploaded images
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/search")
async def search(request: Request, file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Save uploaded image
    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Get recommendations
    results = search_similar_images(file_path)

    # Show results page
    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "uploaded_image": file.filename,
            "results": results
        }
    )