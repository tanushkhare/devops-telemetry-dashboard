# ⚡ DevOps Telemetry Dashboard

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://devops-telemetry-dashboard.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://devops-telemetry-dashboard.vercel.app](https://devops-telemetry-dashboard.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Zero-Trust infrastructure gateway enforcing server-observed IP origin checks and persistent access audit trails.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, JWT RBAC, Prometheus, Uvicorn
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🚀 API Contracts
```http
POST /api/v1/iam/authorize
GET /health
```

---

## 💻 Local Quickstart
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v
```
