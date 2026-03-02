from pydantic import BaseModel, Field
from typing import Optional, List

class PostAnalysisRequest(BaseModel):
    post_id: str = Field(..., example="circle_post_9921")
    content: str = Field(..., min_length=1, example="I found a miracle cure for cancer!")
    author_id: str = Field(..., example="user_443")
    author_name: str

class AnalysisResponse(BaseModel):
    risk_score: float
    decision: str
    label: str
    reason: Optional[str] = None

class CommunityHealthReport(BaseModel):
    overall_sentiment: float
    safety_rating: str
    flagged_count: int
    top_risk_categories: List[str]
    recommendation: str