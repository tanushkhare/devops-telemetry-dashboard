from pydantic import BaseModel

class AccessRequest(BaseModel):
    user_id: str
    role: str
    mfa_verified: bool
    ip_subnet: str

class AccessResponse(BaseModel):
    user_id: str
    access_granted: bool
    token_claims: dict