# Content Moderation ML System

An end-to-end **machine learning–powered content moderation system** designed for real-world integration with web platforms, APIs, and chat applications.

This project demonstrates how an ML model can be trained, deployed as a backend service, and consumed by external applications such as Discord bots or mobile apps.

---

## Features

- Toxic comment detection using Machine Learning  
- TF-IDF + Logistic Regression NLP model  
- REST API built using FastAPI  
- Confidence-based severity classification  
- Real-time Discord bot integration  
- Modular and extensible architecture  

---

## Tech Stack

### Backend & Machine Learning
- Python  
- Scikit-learn  
- NumPy  
- Pandas  
- NLTK  

### API
- FastAPI  
- Uvicorn  

### Integration
- Discord Bot (discord.py)  
- REST-based ML communication  

### Version Control
- Git  
- GitHub  
- Tower (Git GUI)  

---

## System Architecture

```

User Message
↓
Discord Bot / Web App
↓
FastAPI ML Service
↓
ML Model Prediction
↓
Toxicity Result + Confidence
↓
Action (warn / restrict / allow)

````

---

## API Endpoints

### 1. Health Check

**GET /**

Response:
```json
{
  "message": "Content Moderation API running"
}
````

---

### 2. Moderate Content

**POST /moderate**

Request:

```json
{
  "text": "you are stupid"
}
```

Response:

```json
{
  "toxic": true,
  "confidence": 0.87,
  "severity": "high"
}
```

---

## Project Structure

```
content-moderation-ml/
│
├── api/                     # FastAPI backend
│   └── main.py
│
├── preprocessing/           # Text cleaning utilities
│
├── training/                # Model training scripts
│
├── inference/               # Prediction helpers
│
├── models/                  # Trained ML models
│
├── discord_bot/             # Discord moderation bot
│   └── bot.py
│
├── requirements.txt
└── README.md
```

---

## Current Status

* ML model trained and evaluated
* REST API implemented
* Discord bot integrated
* Warning-based moderation system (experimental)
* Designed for future scalability

---

## Future Enhancements

* Multi-language toxicity detection
* Transformer-based models (BERT / RoBERTa)
* Moderation analytics dashboard
* Admin review panel
* Database-backed warning system
* Mobile app integration
* Cloud deployment (Render / Railway / AWS)

---

## Author

**Rakshit Kumar**

This project was built to demonstrate real-world ML deployment, backend integration, and system-level engineering practices.

---

## Note

This repository focuses on **learning, architecture, and engineering workflows**.
Some integrations are under active development and may evolve over time.

