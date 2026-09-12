from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from backend.app.schemas.iam_schema import TokenRequest, TokenResponse, ClusterTelemetry
from backend.app.services.iam_service import iam_service

router = APIRouter(prefix="/api/v1/iam", tags=["DevOps Zero-Trust IAM & Metrics"])

@router.post("/token", response_model=TokenResponse)
async def generate_token(payload: TokenRequest):
    auth_data = iam_service.authenticate_client(payload.client_id, payload.client_secret)
    if not auth_data:
        raise HTTPException(status_code=401, detail="Invalid client credentials.")
    return TokenResponse(**auth_data)

@router.get("/metrics", response_model=ClusterTelemetry)
async def get_metrics(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Missing or malformed Bearer authorization token.")
    return ClusterTelemetry(**iam_service.fetch_cluster_metrics())
