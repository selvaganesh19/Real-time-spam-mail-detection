import base64
import time
from googleapiclient.discovery import build
from model import predict_spam
from db import get_connection

START_TIME = int(time.time())

processed_ids = set()

def get_headers(headers):

    subject = "No Subject"
    sender = "Unknown"

    for h in headers:

        if h["name"] == "Subject":
            subject = h["value"]

        if h["name"] == "From":
            sender = h["value"]

    return sender, subject


def scan_emails(credentials, user_email):

    service = build("gmail", "v1", credentials=credentials)

    conn = get_connection()
    cursor = conn.cursor()

    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        maxResults=10
    ).execute()

    messages = results.get("messages", [])

    for msg in messages:

        msg_id = msg["id"]

        if msg_id in processed_ids:
            continue

        msg_data = service.users().messages().get(
            userId="me",
            id=msg_id,
            format="full"
        ).execute()

        email_time = int(msg_data["internalDate"]) // 1000

        # Skip old mails
        if email_time <= START_TIME:
            processed_ids.add(msg_id)
            continue

        payload = msg_data["payload"]

        sender, subject = get_headers(payload["headers"])

        snippet = msg_data.get("snippet", "")

        label, prob = predict_spam(snippet)

        cursor.execute(
            """
            INSERT INTO email_predictions
            (user_email, sender, subject, prediction, probability)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (user_email, sender, subject, label, float(prob))
        )

        processed_ids.add(msg_id)

    conn.commit()

    cursor.close()
    conn.close()