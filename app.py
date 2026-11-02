from fastapi import FastAPI, UploadFile, File, HTTPException
from detect import analyze_leaf

app = FastAPI(title="Leaf Disease Detection API")

ALLOWED_TYPES = ["image/jpeg", "image/png"]
MAX_SIZE = 4 * 1024 * 1024  # 4 MB


@app.get("/")
def home():
    return {"message": "Leaf Disease Detection API is running"}


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Only JPEG or PNG images are allowed")

    image_bytes = await file.read()

    if len(image_bytes) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="Image is too large (max 4 MB)")

    try:
        return analyze_leaf(image_bytes, file.content_type)
    except Exception:
        raise HTTPException(status_code=502, detail="The analysis service failed. Try again.")