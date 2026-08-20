from fastapi import APIRouter
from app.schemas.iam import AccessRequest, AccessResponse
from app.services.iam_service import verify_zero_trust

router = APIRouter(prefix="/api", tags=["Zero Trust IAM"])

@router.post("/authorize", response_model=AccessResponse)
def authorize_access(payload: AccessRequest):
    return verify_zero_trust(payload)