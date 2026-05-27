"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import patch

import requests

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Validate expected dominant emotions for common inputs."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        """Test the detector with deterministic local fallback output."""
        mock_post.side_effect = requests.RequestException("offline")
        test_cases = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )

        for text_to_analyze, expected_emotion in test_cases:
            with self.subTest(text=text_to_analyze):
                result = emotion_detector(text_to_analyze)
                self.assertEqual(result["dominant_emotion"], expected_emotion)

    def test_blank_input_returns_none(self):
        """Test the required error-handling output for blank text."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
