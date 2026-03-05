import joblib
import re

model = joblib.load("./spam_model.pkl")

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+"," url ",text)

    text = re.sub(r"[^a-zA-Z ]"," ",text)

    return text


def predict_spam(text):

    text = clean_text(text)

    pred = model.predict([text])[0]

    prob = model.predict_proba([text])[0][1]

    label = "SPAM" if pred==1 else "NOT SPAM"

    return label,prob