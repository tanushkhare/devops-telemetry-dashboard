# ⚡ DevOps CI/CD Telemetry Dashboard

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://devops-telemetry-dashboard.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://devops-telemetry-dashboard.vercel.app](https://devops-telemetry-dashboard.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Zero-Trust infrastructure gateway enforcing server-observed IP origin validation and cryptographic JWT authentication with persistent access audit logging.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, JWT RBAC, Prometheus, Uvicorn
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Server-Observed Origin:** Inspects `request.client.host` to prevent header spoofing.
* **Audit Trail Persistence:** Every authorization event is saved to an audit store.
* **Package Consistency:** Clean module imports across all subservices.

---

## 🚀 API Contracts
```http
POST /api/v1/iam/authorize
Headers:
Authorization: Bearer eyJhbGciOi...

Response (200 OK):
{
  "status": "ALLOWED",
  "client_ip": "192.168.1.105",
  "role": "admin",
  "audit_event_id": "audit_84920"
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v