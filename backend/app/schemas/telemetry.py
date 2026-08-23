from pydantic import BaseModel, Field
from typing import List

class TelemetryRequest(BaseModel):
    batch_size: int = Field(default=2500, ge=100, le=100000)
    environment: str = Field(default="Production-Cluster-US-East")

class NodeMetric(BaseModel):
    node_name: str
    cpu_utilization_pct: float
    memory_utilization_pct: float
    active_pods: int
    status: str

class TelemetryResponse(BaseModel):
    cluster_status: str
    avg_cpu_pct: float
    avg_memory_pct: float
    p99_latency_ms: float
    build_success_rate: float
    rollback_recommended: bool
    nodes: List[NodeMetric]
