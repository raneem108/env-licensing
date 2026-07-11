from fastapi import APIRouter
from pydantic import BaseModel
from ai.compliance import check_compliance

router = APIRouter()

class ComplianceRequest(BaseModel):
    activity_type: str
    distance: int

@router.post("/compliance/check/")
def compliance_check(request: ComplianceRequest):
    result = check_compliance(request.activity_type, request.distance)
    return result