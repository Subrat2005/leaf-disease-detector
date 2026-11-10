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
## Run it yourself

1. Install the packages: `pip install -r requirements.txt`
2. Create a file named `.env` containing `GROQ_API_KEY=your_key_here`
3. Start everything with `python run.py`
4. Open http://localhost:8501

## Limitations

The result comes from an AI model, so it can be wrong. It is not a substitute for advice from an agricultural expert.