from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
import json
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from gmail import scan_emails
from google.oauth2.credentials import Credentials
import os

from db import get_connection


app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")


@app.get("/")
def index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))


@app.get("/dashboard.html")
def dashboard():
    return FileResponse(os.path.join(FRONTEND_DIR, "dashboard.html"))


@app.get("/")
def login_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "login.html"))

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
SCOPES = [
'https://www.googleapis.com/auth/gmail.readonly'
]

flow = Flow.from_client_secrets_file(
    "client_secret.json",
    scopes=SCOPES,
    redirect_uri="http://localhost:8000/auth/callback"
)


@app.get("/")
def home():

    return {"message":"Spam SaaS API running"}


# connect gmail
@app.get("/connect-gmail")
def connect_gmail():

    auth_url,state = flow.authorization_url(
        access_type='offline',
        prompt='consent'
    )

    return RedirectResponse(auth_url)
@app.get("/scan-mails")
def scan_mails():

    conn = get_connection()
    cursor = conn.cursor()

    # get stored gmail tokens
    cursor.execute("""
        SELECT access_token, refresh_token
        FROM gmail_tokens
        ORDER BY id DESC
        LIMIT 1
    """)

    token = cursor.fetchone()

    if token:

        access_token, refresh_token = token

        creds = Credentials(
            token=access_token,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=flow.client_config["client_id"],
            client_secret=flow.client_config["client_secret"]
        )

        # scan gmail
        scan_emails(creds, "user@gmail.com")

    cursor.execute("""
        SELECT sender, subject, prediction, probability
        FROM email_predictions
        ORDER BY created_at DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    emails = []

    for row in rows:
        emails.append({
            "sender": row[0],
            "subject": row[1],
            "prediction": row[2],
            "probability": row[3]
        })

    return emails

@app.get("/auth/callback")
def auth_callback(code: str):

    flow.fetch_token(code=code)

    credentials = flow.credentials

    access_token = credentials.token
    refresh_token = credentials.refresh_token

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO gmail_tokens(access_token, refresh_token)
            VALUES (%s,%s)
            """,
            (access_token, refresh_token)
        )

    finally:
        cursor.close()
        conn.close()

    return RedirectResponse("http://127.0.0.1:8000/dashboard.html")



@app.post("/login")
def login(data: dict):

    email=data["email"]
    password=data["password"]

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email,password)
    )

    user=cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return {"success":True}

    return {"success":False}