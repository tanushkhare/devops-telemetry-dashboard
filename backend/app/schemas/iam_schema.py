from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class TokenRequest(BaseModel):
    client_id: str = Field(..., description="Service principal or client ID")
    client_secret: str = Field(..., description="Authentication secret")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_sec: int
    issued_at: str

class ClusterTelemetry(BaseModel):
    cluster_id: str
    cpu_utilization_pct: float
    memory_utilization_pct: float
    network_in_mbps: float
    network_out_mbps: float
    active_pods: int
    health_status: str
    timestamp: str
