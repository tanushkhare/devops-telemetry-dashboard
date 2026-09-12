from fastapi import APIRouter, Request, HTTPException, Header
from typing import Optional
from backend.app.schemas.iam_schema import (
    AuthorizeRequest,
    AuthorizeResponse,
    TokenRequest,
    TokenResponse,
    ClusterTelemetry
)
from backend.app.services.iam_service import iam_service

router = APIRouter(prefix="/api/v1/iam", tags=["DevOps Zero-Trust IAM & Telemetry"])

@router.post("/authorize", response_model=AuthorizeResponse)
async def authorize(request: Request, payload: AuthorizeRequest):
    client_host = request.client.host if request.client else "127.0.0.1"
    result = iam_service.verify_authorization(payload.user_id, payload.role, payload.target_resource, client_host)
    return AuthorizeResponse(**result)

@router.get("/telemetry", response_model=ClusterTelemetry)
async def get_telemetry():
    return ClusterTelemetry(**iam_service.fetch_cluster_metrics())

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
