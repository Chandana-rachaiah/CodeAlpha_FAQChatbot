import re
import nltk
from nltk.corpus import stopwords

# Download English stopwords if they are not already available
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Split the text into words
    words = text.split()

    # Remove common English stopwords
    words = [word for word in words if word not in stop_words]

    # Join the remaining words
    return " ".join(words)