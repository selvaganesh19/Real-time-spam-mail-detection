# 📧 Real-time-spam-mail-detection

Welcome to **Real-time-spam-mail-detection**! This project leverages AI to protect your inbox by identifying spam emails in real time. It integrates seamlessly with Gmail and provides a user-friendly dashboard for monitoring and managing suspicious emails.

---

## 🚀 Introduction

Spam emails are a persistent threat to productivity and security. **Real-time-spam-mail-detection** is designed to intelligently filter and classify emails as spam or not spam using machine learning models. With a modern web interface and instant notifications, you can stay ahead of unwanted messages and keep your inbox clean.

---

## ✨ Features

- **Real-time Gmail Integration**: Connect your Gmail account and scan new emails as they arrive.
- **AI-powered Spam Detection**: Utilizes trained machine learning models to classify emails.
- **Dashboard Analytics**: Visualize and manage detected spam through an easy-to-use web dashboard.
- **Privacy-first**: Includes a clear privacy policy and respects user data.
- **Cross-platform**: Works as a standalone web application (PWA support via manifest).
- **Customizable**: Modular backend design for easy model and database updates.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Node.js (for frontend development, optional)
- PostgreSQL database
- Google Cloud credentials for Gmail API

### Backend Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/selvaganesh19/Real-time-spam-mail-detection.git
    cd Real-time-spam-mail-detection/backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables:
    - Create a `.env` file in the backend directory with your database and Google credentials:
        ```
        DB_HOST=your_db_host
        DB_PORT=your_db_port
        DB_NAME=your_db_name
        DB_USER=your_db_user
        DB_PASSWORD=your_db_password
        ```

4. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Serve static files using any web server (or integrate with backend as static files).

---

## 📈 Usage

1. **Connect Gmail**: Open the web dashboard and click "Connect Gmail". Authenticate with your Google account.
2. **Scan Emails**: The backend will fetch new emails, analyze them, and display spam results on the dashboard.
3. **View Results**: Access `dashboard.html` to see statistics, manage spam, and review privacy policy.
4. **API Usage**: For developers, use FastAPI endpoints to programmatically interact with email scanning and results.

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo and create your branch:
    ```bash
    git checkout -b feature/your-feature
    ```
2. Commit your changes and push:
    ```bash
    git commit -m "Add new feature"
    git push origin feature/your-feature
    ```
3. Open a Pull Request and describe your changes.


---

## 📜 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more information.

---

## 📂 Project Structure

```
Real-time-spam-mail-detection/
│
├── backend/
│   ├── db.py
│   ├── gmail.py
│   ├── main.py
│   ├── model.py
│   └── spam_model.pkl
│
├── frontend/
│   ├── dashboard.html
│   ├── index.html
│   ├── manifest.json
│   ├── privacy.html
│   └── script.js
│
└── README.md
```

---

## 💡 Get Started Today!

Protect your inbox with the power of AI.  
Star ⭐ the repo and feel free to open issues or feature requests!

---


## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/selvaganesh19/Real-time-spam-mail-detection