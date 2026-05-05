# Mini AI Chatbot (Fullstack)

A modern, fullstack AI chatbot application featuring a sleek React frontend and a robust FastAPI backend. It utilizes Cloudflare Workers AI with Meta's LLaMA 3 model to provide intelligent, conversational responses with persistent memory.

---

## 🚀 Features

-   **Premium Glassmorphism UI**: A stunning, modern interface with transparency, blur effects, and vibrant gradients.
-   **Persistent Memory**: Chat history is saved in a local `chat_history.json` file on the backend.
-   **Smart Context Management**: Automatically trims history (sending only the last 10 messages) to stay within AI context limits and save tokens.
-   **Secure Credentials**: API keys are managed securely via a `.env` file.
-   **Fast & Responsive**: Built with FastAPI for high-performance backend logic and React for a "snappy" user experience.
-   **Enter to Send**: Support for keyboard interactions in the chat.

---

## 🛠️ Tech Stack

-   **Backend**: Python 3.x, FastAPI, Uvicorn, Requests, Python-dotenv.
-   **Frontend**: React (TypeScript), Tailwind CSS, Lucide Icons.
-   **AI Engine**: Cloudflare Workers AI (@cf/meta/llama-3-8b-instruct).

---

## 📂 Project Structure

```text
/Mini AI Chatbot
├── chatbot.py           # Core AI logic (API calls & history management)
├── main.py              # FastAPI server entry point
├── .env                 # API keys (hidden)
├── .gitignore           # Files to ignore in Git
├── requirements.txt     # Python dependencies list
├── chat_history.json    # Local database for chat logs
└── /chatbot-ui          # React Frontend Folder
    ├── /src
    │   ├── /components  # Modular UI parts (Header, Message, Input)
    │   ├── App.tsx      # Main frontend logic
    │   └── index.css    # Tailwind & global styles
    └── tailwind.config.js
```

---

## ⚙️ Setup Instructions

### 1. Backend Setup (Python)

1.  **Create a Virtual Environment**:
    ```powershell
    python -m venv .venv
    .venv\Scripts\activate
    ```
2.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your Cloudflare credentials:
    ```env
    CLOUDFLARE_API_TOKEN=your_api_token_here
    CLOUDFLARE_ACCOUNT_ID=your_account_id_here
    ALLOWED_ORIGINS=http://localhost:3000,https://your-site.vercel.app
    ```

### 2. Frontend Setup (React)

1.  **Navigate to the UI folder**:
    ```powershell
    cd chatbot-ui
    ```
2.  **Install Dependencies**:
    ```powershell
    npm install
    ```
3.  **Configure Environment Variables**:
    Create a `.env` file in the `chatbot-ui` folder:
    ```env
    REACT_APP_API_URL=http://localhost:8000
    ```

---

## 🏃 How to Run

You need **two terminals** open to run the full application:

### Terminal 1: Start Backend
```powershell
uvicorn main:app --reload
```
*The backend will run at `http://127.0.0.1:8000`*

### Terminal 2: Start Frontend
```powershell
cd chatbot-ui
npm start
```
*The frontend will open in your browser at `http://localhost:3000`*

---

## 📝 License
MIT License - Created with ❤️ by Mandeep.
