import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_authorized_devops_access():
    payload = {
        "user_id": "usr_test_admin",
        "role": "admin",
        "target_resource": "cluster/k8s/nodes"
    }
    res = client.post("/api/v1/iam/authorize", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["access_granted"] is True
    assert "ZTI-" in data["auth_token"]
    assert data["assigned_role"] == "admin"

def test_unauthorized_role_rejection():
    payload = {
        "user_id": "usr_test_guest",
        "role": "guest_viewer",
        "target_resource": "cluster/k8s/nodes"
    }
    res = client.post("/api/v1/iam/authorize", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["access_granted"] is False
    assert data["auth_token"] is None

def test_cluster_telemetry():
    res = client.get("/api/v1/iam/telemetry")
    assert res.status_code == 200
    data = res.json()
    assert "k8s" in data["cluster_id"]
    assert data["active_pods"] > 0
