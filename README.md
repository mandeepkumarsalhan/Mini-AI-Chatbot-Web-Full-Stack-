# Mini AI Chatbot — Full Stack

A modern full-stack AI chatbot application with a **Python FastAPI backend** and a **React TypeScript frontend**. Powered by **Cloudflare Workers AI** (Meta LLaMA 3) for intelligent, conversational responses with persistent chat memory.

---

## ✨ Features

- **Glassmorphism UI** — sleek dark interface with blur effects and vibrant gradients
- **Persistent Memory** — chat history saved locally in `chat_history.json`
- **Smart Context Trimming** — sends only last 10 messages to avoid token limits
- **Secure Credentials** — API keys managed via `.env` files (never committed)
- **CORS Configured** — whitelist specific frontend origins for security
- **Keyboard Accessible** — press `Enter` to send messages

---

## 🛠️ Tech Stack

| Layer     | Technology                                      |
|-----------|-------------------------------------------------|
| Backend   | Python 3.x, FastAPI, Uvicorn, Python-dotenv     |
| Frontend  | React 19, TypeScript, Tailwind CSS, Lucide Icons |
| AI Engine | Cloudflare Workers AI (`@cf/meta/llama-3-8b-instruct`) |

---

## 📂 Project Structure

```text
Mini AI Chatbot/
├── backend/                    # Python FastAPI backend
│   ├── main.py                 # API server entry point
│   ├── chatbot.py              # Cloudflare AI logic & history
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # ⚠️ Real credentials (gitignored)
│   └── .env.example            # Template — copy and fill in
│
├── frontend/                   # React TypeScript frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatHeader.tsx
│   │   │   ├── ChatInput.tsx
│   │   │   └── ChatMessage.tsx
│   │   ├── App.tsx             # Main app logic
│   │   └── index.css           # Tailwind & global styles
│   ├── .env                    # ⚠️ Frontend env (gitignored)
│   ├── .env.example            # Template — copy and fill in
│   ├── package.json
│   └── tailwind.config.js
│
├── .gitignore                  # Root-level ignore rules
└── README.md
```

---

## ⚙️ Setup

### Prerequisites

- Python 3.9+
- Node.js 18+ and npm
- A [Cloudflare account](https://dash.cloudflare.com) with Workers AI enabled

---

### 1. Backend Setup

```powershell
cd backend
```

**Create and activate a virtual environment:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Install dependencies:**
```powershell
pip install -r requirements.txt
```

**Configure environment variables:**

Copy the example file and fill in your credentials:
```powershell
Copy-Item .env.example .env
```

Edit `backend/.env`:
```env
CLOUDFLARE_API_TOKEN=your_api_token_here
CLOUDFLARE_ACCOUNT_ID=your_account_id_here
ALLOWED_ORIGINS=http://localhost:3000
```

> Get your credentials from [Cloudflare Dashboard → API Tokens](https://dash.cloudflare.com/profile/api-tokens)

---

### 2. Frontend Setup

```powershell
cd frontend
```

**Install dependencies:**
```powershell
npm install
```

**Configure environment variables:**

```powershell
Copy-Item .env.example .env
```

Edit `frontend/.env`:
```env
REACT_APP_API_URL=http://localhost:8000
```

---

## 🏃 Running the App

You need **two terminals** running simultaneously.

### Terminal 1 — Start Backend

```powershell
cd backend
.venv\Scripts\activate
uvicorn main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`  
API docs at: `http://127.0.0.1:8000/docs`

### Terminal 2 — Start Frontend

```powershell
cd frontend
npm start
```

Frontend opens at: `http://localhost:3000`

---

## 🔌 API Endpoints

| Method | Endpoint | Description          |
|--------|----------|----------------------|
| GET    | `/`      | Health check         |
| POST   | `/chat`  | Send a chat message  |

**POST `/chat` — Request body:**
```json
{ "message": "Hello!" }
```

**Response:**
```json
{ "response": "Hi there! How can I help you today?" }
```

---

## Live Demo
- 🌐 [Live Demo](https://mini-ai-chatbot-web-full-stack.vercel.app/)
- <img width="1868" height="952" alt="image" src="https://github.com/user-attachments/assets/13ace0e5-4f3d-482e-82a5-5001d7b89aa4" />

--- 
## 📝 License

MIT License — Created with ❤️ by Mandeep.
