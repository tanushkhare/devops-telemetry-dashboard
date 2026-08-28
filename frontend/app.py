import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DevOps Telemetry Dashboard", layout="wide")

st.title("🛡️ Zero-Trust IAM & DevOps Telemetry Control Plane")
st.markdown("Role-Based Access Control authorization, server-observed client host validation, and real-time cluster telemetry.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("IAM Access Gate Ingestion")
    user_id = st.text_input("Principal User ID", value="usr_devops_901")
    role = st.selectbox("Requested Operational Role", ["devops_engineer", "admin", "sre_lead", "guest_viewer"])
    resource = st.text_input("Target Resource Scope", value="cluster/k8s-prod-us-east/nodes")

    if st.button("Request Zero-Trust Token", type="primary"):
        with st.spinner("Evaluating origin IP and RBAC role policies..."):
            try:
                res = requests.post(
                    "http://localhost:8000/api/v1/iam/authorize",
                    json={"user_id": user_id, "role": role, "target_resource": resource},
                    timeout=5
                )
                if res.status_code == 200:
                    st.session_state["p16_auth"] = res.json()
                    st.success("IAM Evaluation Executed!")
                else:
                    st.error(f"IAM Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Running client-side authentication simulation.")
                is_granted = role != "guest_viewer"
                st.session_state["p16_auth"] = {
                    "user_id": user_id,
                    "access_granted": is_granted,
                    "assigned_role": role if is_granted else "DENIED",
                    "client_ip": "127.0.0.1",
                    "security_context": "MUTUAL_TLS_AND_RBAC_VERIFIED" if is_granted else "INSUFFICIENT_RBAC_PRIVILEGES",
                    "auth_token": "ZTI-SIM8812AF901" if is_granted else None,
                    "reason": f"Authorization confirmed for {role}." if is_granted else "Insufficient role privileges.",
                    "timestamp": "2026-08-28T09:45:00Z"
                }

with col2:
    if "p16_auth" in st.session_state:
        auth = st.session_state["p16_auth"]
        st.subheader("IAM Token & Security Audit")
        
        m1, m2 = st.columns(2)
        m1.metric("Principal", auth["user_id"])
        m2.metric("Access Decision", "GRANTED" if auth["access_granted"] else "REJECTED", delta=auth["assigned_role"])
        
        if auth["access_granted"]:
            st.success(f"🔑 Auth Token: `{auth['auth_token']}`")
            st.info(f"Security Context: `{auth['security_context']}` | Host IP: `{auth['client_ip']}`")
        else:
            st.error(f"❌ {auth['reason']}")
            
        # Simulated live Kubernetes telemetry
        st.markdown("### 📊 Cluster Health Harvester")
        telem_df = pd.DataFrame({
            "Resource": ["CPU Utilization", "Memory Usage", "Network In (Mbps/10)", "Network Out (Mbps/10)"],
            "Percentage / Scale": [42.8, 68.4, 12.8, 34.2]
        })
        fig = px.bar(telem_df, x="Resource", y="Percentage / Scale", color="Resource", title="Live Node Telemetry (k8s-prod-us-east-1)")
        st.plotly_chart(fig, use_container_width=True)
