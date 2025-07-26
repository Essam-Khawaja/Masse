# 🧙 AI Dungeon Master – Masse

An AI-powered Dungeon Master that crafts dynamic fantasy RPG adventures. Built for the Agentic AI Hackathon.

## Features
- Generate 3-act fantasy campaigns using Gemini API
- Let players interact freely with the story
- Beautiful, markdown-enhanced storytelling

## Tech Stack
- Frontend: Next.js 15
- Backend: FastAPI (Python)
- LLM: Gemini 2.5 Flash
- State: Local JSON for plan memory

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/Essam-Khawaja/Masse
cd Masse
```

### 2. Backend Setup
- Create a `.env` file:
```ini
GEMENI_API_KEY=your_gemini_key
```
- Run the backend:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run build
npm run start
```

