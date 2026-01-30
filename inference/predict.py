import joblib
from preprocessing.clean_text import clean_text

model = joblib.load("models/toxic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_toxicity(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prob = model.predict_proba(vec)[0][1]

    return {
        "toxic": prob > 0.5,
        "confidence": round(float(prob), 3)
    }

if __name__ == "__main__":
    text = input("Enter comment: ")
    print(predict_toxicity(text))
