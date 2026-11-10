import subprocess
import sys

# Start the backend (API) and the frontend (page) at the same time
backend = subprocess.Popen([sys.executable, "-m", "uvicorn", "app:app", "--reload"])
frontend = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "frontend/frontend.py"])
try:
    backend.wait()
    frontend.wait()
except KeyboardInterrupt:
    backend.terminate()
    frontend.terminate()