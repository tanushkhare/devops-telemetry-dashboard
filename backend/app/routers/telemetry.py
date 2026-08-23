from fastapi import APIRouter
from backend.app.schemas.telemetry import TelemetryRequest, TelemetryResponse
from backend.app.services.telemetry_service import telemetry_service

router = APIRouter(prefix="/api/v1/telemetry", tags=["DevOps Telemetry Engine"])

@router.post("/query", response_model=TelemetryResponse)
async def query_cluster_metrics(payload: TelemetryRequest):
    return telemetry_service.get_cluster_telemetry(payload)
