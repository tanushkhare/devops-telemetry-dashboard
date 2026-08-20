from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import iam

app = FastAPI(title="Zero-Trust IAM API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(iam.router)

@app.get("/")
def read_root():
    return {"message": "Zero-Trust IAM Gateway is online!"}