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
    cleaned = clean_text(request.text)
    vec = vectorizer.transform([cleaned])
    prob = model.predict_proba(vec)[0][1]

    severity = "low"
    if prob > 0.8:
        severity = "high"
    elif prob > 0.5:
        severity = "medium"

    return {
    "toxic": bool(prob > 0.5),
    "confidence": float(round(prob, 3)),
    "severity": severity
}

