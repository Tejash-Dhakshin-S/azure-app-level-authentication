from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Doc Receiver API", version="1.0.0")

# Optional: helps during local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/receive-document")
async def receive_document(file: UploadFile = File(...)):
    data = await file.read()
    size = len(data)
    # Your “simple function” placeholder (you will replace later)
    return {
        "message": "File received successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": size,
    }
