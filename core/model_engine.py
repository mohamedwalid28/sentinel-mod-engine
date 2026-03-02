import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

class ModerationModel:
    """
    A lightweight NLP pipeline trained to distinguish between 
    safe community talk and dangerous/toxic medical misinformation.
    """
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
            ('clf', LogisticRegression(C=1.0))
        ])
        self._train_mock_data()

    def _train_mock_data(self):
        # 0 = Safe, 1 = Unsafe (Toxic/Misinformation)
        X = [
            "How do I manage chemo fatigue?", 
            "I found a miracle 24-hour cancer cure online!", 
            "You are all idiots for believing this.",
            "Thank you doctor for the integrated medicine tips.",
            "Stop your medication and eat only lemon rinds to cure cancer."
        ]
        y = [0, 1, 1, 0, 1]
        self.pipeline.fit(X, y)

    def predict_risk(self, text: str):
        prob = self.pipeline.predict_proba([text])[0][1]
        return round(float(prob), 4)

# Global Instance
engine = ModerationModel()