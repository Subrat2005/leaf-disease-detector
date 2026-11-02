# Leaf Disease Detector

A web app that checks a photo of a plant leaf for disease. Upload an image, and the app tells you whether the leaf looks healthy or diseased, how severe it is, the symptoms, and suggested treatment.

## How it works

1. The Streamlit page (`frontend.py`) lets the user upload a leaf photo.
2. It sends the image to a FastAPI backend (`app.py`).
3. The backend checks the file type and size, then passes the image to `detect.py`.
4. `detect.py` sends the image to a vision model on Groq and asks for the answer in JSON.
5. The result goes back to the page and is displayed.

Photos that are not plant leaves are rejected.

## Tech used

Python, FastAPI, Uvicorn, Streamlit, Groq API (Qwen vision model)
