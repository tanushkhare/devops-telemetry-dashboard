from fastapi import APIRouter, Request, HTTPException
from backend.app.schemas.iam_schema import AuthorizeRequest, AuthorizeResponse, TelemetryMetricsResponse
from backend.app.services.iam_service import iam_service

router = APIRouter(prefix="/api/v1/iam", tags=["Zero-Trust IAM & Telemetry Gateway"])

@router.post("/authorize", response_model=AuthorizeResponse)
async def authorize_access(request: Request, payload: AuthorizeRequest):
    # Server-observed client host inspection
    client_host = request.client.host if request.client else "127.0.0.1"
    result = iam_service.verify_authorization(payload.user_id, payload.role, payload.target_resource, client_host)
    return AuthorizeResponse(**result)

@router.get("/telemetry", response_model=TelemetryMetricsResponse)
async def get_telemetry():
    return TelemetryMetricsResponse(**iam_service.get_cluster_telemetry())
