def verify_zero_trust(req):
    granted = req.mfa_verified and req.role in ["admin", "engineer"] and req.ip_subnet.startswith("10.")
    claims = {
        "sub": req.user_id,
        "role": req.role,
        "scope": "full-read-write" if granted else "restricted"
    }
    return {
        "user_id": req.user_id,
        "access_granted": granted,
        "token_claims": claims
    }