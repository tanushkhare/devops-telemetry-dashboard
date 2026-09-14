import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #090d16;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        .sidebar .stSidebar {
            background-color: #0f172a;
            border-right: 1px solid #1e293b;
        }
        h1, h2, h3 {
            color: #f8fafc;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        .stButton>button {
            background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
            color: #090d16;
            font-weight: 600;
            border: none;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="DevOps Telemetry Hub", layout="wide")

st.title("🛡️ Zero-Trust DevOps Telemetry Dashboard")
st.markdown("Real-time telemetry streaming and infrastructure monitoring.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("IAM Access Token")
    cid = st.text_input("Client ID", value="svc_devops_monitoring")
    csec = st.text_input("Client Secret", value="devops-telemetry-secret-2026", type="password")

    if st.button("Authenticate & Ingest Metrics", type="primary"):
        try:
            tok_res = requests.post("http://localhost:8000/api/v1/iam/token", json={"client_id": cid, "client_secret": csec}, timeout=5)
            if tok_res.status_code == 200:
                token = tok_res.json()["access_token"]
                m_res = requests.get("http://localhost:8000/api/v1/iam/metrics", headers={"Authorization": f"Bearer {token}"}, timeout=5)
                if m_res.status_code == 200:
                    st.session_state["p16_data"] = m_res.json()
                    st.success("Authorized: Metrics ingested successfully.")
                else:
                    st.error(f"Metrics fetch error: {m_res.text}")
            else:
                st.error("Authentication failed.")
        except Exception:
            st.warning("Backend offline. Loading local telemetry fallback.")
            st.session_state["p16_data"] = {
                "cluster_id": "k8s-prod-us-east",
                "cpu_utilization_pct": 68.4,
                "memory_utilization_pct": 74.2,
                "network_in_mbps": 124.5,
                "network_out_mbps": 89.2,
                "active_pods": 48,
                "health_status": "HEALTHY_OPTIMAL",
                "timestamp": "2026-08-28T09:30:00Z"
            }

with col2:
    if "p16_data" in st.session_state:
        d = st.session_state["p16_data"]
        st.subheader(f"Cluster: {d['cluster_id']}")
        m1, m2, m3 = st.columns(3)
        m1.metric("CPU Load", f"{d['cpu_utilization_pct']}%")
        m2.metric("Memory Usage", f"{d['memory_utilization_pct']}%")
        m3.metric("Active Pods", d["active_pods"])

        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = d["cpu_utilization_pct"],
            title = {"text": "CPU Utilization (%)"},
            gauge = {"axis": {"range": [None, 100]}, "bar": {"color": "#38bdf8"}}
        ))
        st.plotly_chart(fig, use_container_width=True)

