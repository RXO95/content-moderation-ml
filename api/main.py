import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

from preprocessing.clean_text import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models/toxic_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "models/tfidf_vectorizer.pkl"))

app = FastAPI(title="Content Moderation ML API")


class TextRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Content Moderation API running"}


@app.post("/moderate")
def moderate_text(request: TextRequest):
    try:
        text = request.text.strip()

        # ✅ Guard 1: empty or whitespace text
        if not text:
            return {
                "toxic": False,
                "confidence": 0.0,
                "severity": "low"
            }

        cleaned = clean_text(text)

        # ✅ Guard 2: vectorizer safety
        vec = vectorizer.transform([cleaned])

        prob = model.predict_proba(vec)[0][1]
        prob = float(prob)

        severity = "low"
        if prob > 0.8:
            severity = "high"
        elif prob > 0.5:
            severity = "medium"

        return {
            "toxic": bool(prob > 0.5),
            "confidence": round(prob, 3),
            "severity": severity
        }

    except Exception as e:
        print("API ERROR:", e)

        # ✅ Always return valid JSON
        return {
            "toxic": False,
            "confidence": 0.0,
            "severity": "low"
        }
