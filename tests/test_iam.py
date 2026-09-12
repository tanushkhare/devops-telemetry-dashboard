import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_token_and_metrics_auth():
    # Valid auth
    t_res = client.post("/api/v1/iam/token", json={"client_id": "monitoring", "client_secret": "devops-telemetry-secret-2026"})
    assert t_res.status_code == 200
    token = t_res.json()["access_token"]

    # Ingest metrics with Bearer
    m_res = client.get("/api/v1/iam/metrics", headers={"Authorization": f"Bearer {token}"})
    assert m_res.status_code == 200
    assert m_res.json()["cluster_id"] == "k8s-prod-us-east"

def test_unauthorized_metrics_access():
    m_res = client.get("/api/v1/iam/metrics")
    assert m_res.status_code == 403
