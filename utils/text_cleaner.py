import re


def clean_text(text):
    """
    Clean extracted PDF text.
    """

    # Replace multiple newlines with one newline
    text = re.sub(r"\n+", "\n", text)

    # Replace multiple spaces with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text