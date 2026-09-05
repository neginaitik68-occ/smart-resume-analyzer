import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Convert text into individual words
    words = word_tokenize(text)

    # Remove common English words
    stop_words = set(stopwords.words("english"))

    words = [
        word for word in words
        if word not in stop_words
    ]

    # Convert words back into text
    cleaned_text = " ".join(words)

    return cleaned_text