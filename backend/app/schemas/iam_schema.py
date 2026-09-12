from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class AuthorizeRequest(BaseModel):
    user_id: str = Field(..., description="Identity principal / IAM subject")
    role: str = Field(default="devops_engineer", description="Requested role: admin, devops_engineer, sre_lead, guest_viewer")
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
