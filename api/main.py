from fastapi import FastAPI
from core.model_engine import engine
from core.guardian import GuardianLogic

app = FastAPI(title="Sentinel Moderation API")

@app.post("/analyze")
async def analyze_post(content: str, user_id: str):
    score = engine.predict_risk(content)
    decision = GuardianLogic.evaluate_content(score)
    
    return {
        "user_id": user_id,
        "risk_score": score,
        "decision": decision
    }

@app.get("/community-health")
async def get_metrics():
    # Mock health metrics for the oncologist's dashboard
    return {
        "sentiment_score": 0.82, # Out of 1.0
        "safety_rating": "Excellent",
        "flagged_today": 4
    }