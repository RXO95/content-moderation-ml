import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from preprocessing.clean_text import clean_text


df = pd.read_csv("data/train.csv")


df["toxic_label"] = df[
    ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
].max(axis=1)

df["clean_comment"] = df["comment_text"].apply(clean_text)

X = df["clean_comment"]
y = df["toxic_label"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


vectorizer = TfidfVectorizer(max_features=20000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)


y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))


joblib.dump(model, "models/toxic_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("Model trained and saved successfully.")
