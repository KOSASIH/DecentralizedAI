import spacy

def preprocess_text(text: str) -> str:
    """
    Perform text preprocessing to clean and normalize input text.

    Args:
    text (str): The input text to preprocess.

    Returns:
    str: The preprocessed text.
    """

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    preprocessed_text = ""
    for token in doc:
        preprocessed_text += token.lemma_ + " "

    return preprocessed_text.strip()

def detect_language(text: str) -> str:
    """
    Detect the language of the input text.

    Args:
    text (str): The input text to detect the language.

    Returns:
    str: The detected language of the input text.
    """

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    return doc.lang_

def analyze_sentiment(text: str) -> chr:
    """
    Perform sentiment analysis on the input text.

    Args:
    text (str): The input text to analyze the sentiment.

    Returns:
    chr: The sentiment label of the input text.
    """

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    sentiment_score = doc.sentiment["polarity"]

    if sentiment_score > 0.5:
        return "+"
    elif sentiment_score < -0.5:
        return "-"
    else:
        return "0"

def extract_entities(text: str) -> list:
    """
    Extract named entities from the input text.

    Args:
    text (str): The input text to extract named entities.

    Returns:
    list: The list of named entities.
    """

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    entities = []
    for entity in doc.ents:
        entities.append((entity.text, entity.label_))

    return entities
