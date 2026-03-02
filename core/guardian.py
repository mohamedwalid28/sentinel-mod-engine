class GuardianLogic:
    """
    Translates ML scores into business actions for a Community Manager.
    """
    @staticmethod
    def evaluate_content(risk_score: float):
        if risk_score > 0.85:
            return {
                "action": "AUTO_REJECT",
                "label": "DANGEROUS",
                "reason": "High probability of medical misinformation or extreme toxicity."
            }
        elif risk_score > 0.50:
            return {
                "action": "FLAG_FOR_REVIEW",
                "label": "SUSPICIOUS",
                "reason": "Potential community guideline violation."
            }
        return {"action": "ALLOW", "label": "SAFE", "reason": None}