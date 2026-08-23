from backend.app.schemas.telemetry import TelemetryRequest, TelemetryResponse, NodeMetric

class DevOpsTelemetryEngine:
    @staticmethod
    def get_cluster_telemetry(payload: TelemetryRequest) -> TelemetryResponse:
        nodes = [
            NodeMetric(node_name="k8s-worker-node-01", cpu_utilization_pct=42.5, memory_utilization_pct=68.2, active_pods=34, status="HEALTHY"),
            NodeMetric(node_name="k8s-worker-node-02", cpu_utilization_pct=78.9, memory_utilization_pct=84.1, active_pods=48, status="WARNING"),
            NodeMetric(node_name="k8s-worker-node-03", cpu_utilization_pct=36.1, memory_utilization_pct=52.4, active_pods=28, status="HEALTHY"),
            NodeMetric(node_name="k8s-worker-node-04", cpu_utilization_pct=51.0, memory_utilization_pct=61.8, active_pods=39, status="HEALTHY")
        ]

        avg_cpu = round(sum(n.cpu_utilization_pct for n in nodes) / len(nodes), 1)
        avg_mem = round(sum(n.memory_utilization_pct for n in nodes) / len(nodes), 1)
        p99 = round(12.4 + (payload.batch_size / 2500.0) * 1.8, 1)
        success_rate = 99.1

        rollback = avg_cpu > 80.0 or avg_mem > 85.0

        return TelemetryResponse(
            cluster_status="OPTIMAL" if not rollback else "DEGRADED",
            avg_cpu_pct=avg_cpu,
            avg_memory_pct=avg_mem,
            p99_latency_ms=p99,
            build_success_rate=success_rate,
            rollback_recommended=rollback,
            nodes=nodes
        )

telemetry_service = DevOpsTelemetryEngine()
