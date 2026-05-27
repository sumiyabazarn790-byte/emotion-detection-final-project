"""Emotion detection helpers using the Watson NLP service."""

import json
import re

import requests


WATSON_EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_response():
    """Return the required output shape for invalid input."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def _format_response(scores):
    """Convert raw emotion scores into the required project format."""
    dominant_emotion = max(scores, key=scores.get)
    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }


def _fallback_scores(text_to_analyze):
    """Provide deterministic local scores when the remote service is unavailable."""
    keywords = {
        "anger": {
            "angry",
            "mad",
            "furious",
            "rage",
            "annoyed",
            "irritated",
        },
        "disgust": {
            "disgust",
            "disgusted",
            "gross",
            "nasty",
            "revolting",
            "sickening",
        },
        "fear": {
            "afraid",
            "fear",
            "fearful",
            "scared",
            "terrified",
            "worried",
        },
        "joy": {
            "glad",
            "happy",
            "joy",
            "joyful",
            "delighted",
            "excited",
            "love",
        },
        "sadness": {
            "sad",
            "sadness",
            "unhappy",
            "depressed",
            "miserable",
            "heartbroken",
        },
    }
    words = set(re.findall(r"[a-z']+", text_to_analyze.lower()))
    raw_scores = {
        emotion: len(words.intersection(emotion_keywords))
        for emotion, emotion_keywords in keywords.items()
    }

    total_score = sum(raw_scores.values())
    if total_score == 0:
        return _empty_response()

    scores = {
        emotion: round(raw_scores[emotion] / total_score, 6)
        for emotion in EMOTIONS
    }
    return _format_response(scores)


def emotion_detector(text_to_analyze):
    """Analyze text and return anger, disgust, fear, joy, sadness, and dominant emotion."""
    if not text_to_analyze or not text_to_analyze.strip():
        return _empty_response()

    payload = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": WATSON_MODEL_ID}

    try:
        response = requests.post(
            WATSON_EMOTION_URL,
            json=payload,
            headers=headers,
            timeout=8,
        )
    except requests.RequestException:
        return _fallback_scores(text_to_analyze)

    if response.status_code == 400:
        return _empty_response()

    response.raise_for_status()
    formatted_response = json.loads(response.text)
    scores = formatted_response["emotionPredictions"][0]["emotion"]
    return _format_response(scores)
