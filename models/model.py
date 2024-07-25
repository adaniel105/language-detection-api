import pickle
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/language-detection.pkl", "rb") as f:
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


def prediction_pipeline(text):
    text = re.sub(
        r"['!@#$(),\n%^*?\:;~0-9']", " ", text
    )  # replaces all special characters in text with empty strings
    text = re.sub(r"[[]]", " ", text)  # replaces square brackets with empty strings
    predictions = model.predict([text])
    return classes[predictions[0]]
