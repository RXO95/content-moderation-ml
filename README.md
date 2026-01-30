# Content Moderation ML System

An ML-powered toxic comment and content moderation system designed to be integrated into web applications, bots, and mobile platforms.

## Features
- Toxic comment detection using machine learning
- TF-IDF + Logistic Regression model
- REST API built with FastAPI
- Confidence scoring and severity levels
- Ready for Discord bot and mobile app integration

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- NLP (TF-IDF)
- REST APIs

## API Endpoints

### Health Check
GET /


### Moderate Content

POST /moderate


Request:
```bash
json
{
  "text": "you are stupid"
}
```
Response:
```bash
{
  "toxic": true,
  "confidence": 0.87,
  "severity": "high"
}
```
## Project Structure
```bash
content-moderation-ml/
├── api/
├── preprocessing/
├── training/
├── inference/
├── models/
└── requirements.txt
```

## Future Enhancements

Discord moderation bot

Mobile app integration

Multi-language support

Transformer-based model upgrade

Admin moderation dashboard

## Author

Rakshit Kumar
