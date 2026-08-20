import streamlit as st
import requests

st.title("🔐 Zero-Trust IAM Access Control Gateway")
uid = st.text_input("User ID", "nidhi_admin")
role = st.selectbox("Assigned Role", ["admin", "engineer", "guest"])
mfa = st.checkbox("MFA Token Authenticated", value=True)
ip = st.text_input("IP Subnet", "10.0.0.45")

if st.button("Evaluate Zero-Trust Request"):
    res = requests.post("http://127.0.0.1:8000/api/authorize", json={
        "user_id": uid, "role": role, "mfa_verified": mfa, "ip_subnet": ip
    })
    if res.status_code == 200:
        data = res.json()
        if data["access_granted"]:
            st.success("✅ Access Granted by Zero-Trust Engine")
        else:
            st.error("⛔ Access Denied: Policy Violation or Untrusted Context")
        st.json(data["token_claims"])