"""Flask web application for detecting emotions in text."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


def format_emotion_response(emotion_response):
    """Build the project-required user-facing response string."""
    return (
        "For the given statement, the system response is "
        f"'anger': {emotion_response['anger']}, "
        f"'disgust': {emotion_response['disgust']}, "
        f"'fear': {emotion_response['fear']}, "
        f"'joy': {emotion_response['joy']} and "
        f"'sadness': {emotion_response['sadness']}. "
        f"The dominant emotion is {emotion_response['dominant_emotion']}."
    )


@app.route("/emotionDetector")
def detect_emotion():
    """Run emotion detection for the text supplied by the web page."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    emotion_response = emotion_detector(text_to_analyze)

    if emotion_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return format_emotion_response(emotion_response)


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
