from pydantic import BaseModel
from typing import List

class CombinedRequest(BaseModel):
    activity_type: str
    distance: int
    question: str

class CombinedResponse(BaseModel):
    activity_type: str
    category: str
    approved: bool
    required_distance: int
    provided_distance: int
    reason: str
    regulation_answer: str
    sources: List[str]