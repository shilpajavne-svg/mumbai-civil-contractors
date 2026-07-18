from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
import shutil
import os

app = FastAPI(title="Mumbai Civil Works API")

# Allow your website to talk to your backend safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a folder to store uploaded site photos
UPLOAD_DIR = "uploaded_photos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Mumbai Civil Contractors API is running successfully! Call 7757838070"}

@app.post("/upload-photo/")
async def upload_photo(file: UploadFile = File(...)):
    """API Endpoint to upload project construction photos"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save the file securely on the server
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {
        "status": "success",
        "message": f"Photo '{file.filename}' uploaded successfully for Mumbai Civil Works!",
        "file_path": file_path
    }

if __name__ == "__main__":
    uvicorn.run(main, host="0.0.0.0", port=8000)
