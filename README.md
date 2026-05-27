# Emotion Detection Final Project

This project implements a Flask web application that detects emotions in text
using the Watson NLP emotion prediction service.

## Run

```bash
pip install -r requirements.txt
python server.py
```

Open `http://localhost:5000`.

## Test

```bash
python -m unittest test_emotion_detection.py
python -m pylint server.py
```
