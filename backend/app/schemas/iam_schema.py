from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class AuthorizeRequest(BaseModel):
    user_id: str = Field(..., description="Identity principal / IAM subject")
    role: str = Field(default="devops_engineer", description="Role requested: devops_engineer, admin, or viewer")
    target_resource: str = Field(default="cluster/k8s-prod-us-east/nodes")

class AuthorizeResponse(BaseModel):
    user_id: str
    access_granted: bool
    assigned_role: str
    client_ip: str
    security_context: str
    auth_token: Optional[str] = None
    reason: str
    timestamp: str

class TelemetryMetricsResponse(BaseModel):
    cluster_id: str
    cpu_utilization_pct: float
    memory_utilization_pct: float
    network_in_mbps: float
    network_out_mbps: float
    active_pods: int
    health_status: str
    timestamp: str
