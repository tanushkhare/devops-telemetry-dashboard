from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import iam
import uvicorn

app = FastAPI(
    title="DevOps Zero-Trust IAM & Telemetry Gateway API",
    description="Role-Based Access Control (RBAC), client host origin verification, and Kubernetes telemetry harvester.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(iam.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "devops-telemetry-dashboard"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
