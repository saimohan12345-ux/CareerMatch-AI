import re


def clean_text(text):

    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary characters
    text = re.sub(r"[^a-zA-Z0-9+#./ -]", " ", text)

    return text.strip()