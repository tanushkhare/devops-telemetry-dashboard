from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers.telemetry import router as telemetry_router
import uvicorn

app = FastAPI(
    title="DevOps CI/CD & Infrastructure Telemetry API",
    description="Prometheus infrastructure scraping, Kubernetes cluster health metrics, and build telemetry.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(telemetry_router)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "devops-telemetry-dashboard"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
