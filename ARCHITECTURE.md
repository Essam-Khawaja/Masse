# 🏗️ Architecture Overview – AI Dungeon Master

## Components

### 1. **User Interface**
- **Frontend:** Next.js 15
- **Role:** Users enter prompts and view AI responses

---

### 2. **Agent Core**

```plaintext
        +------------------------+
        |   User Input (UI)     |
        +-----------+------------+
                    |
                    ▼
         +----------+-----------+
         |      FastAPI Server   |
         |       (main.py)       |
         +----+-----------+------+
              |           |
     +--------+--+   +----+---------+
     | planner.py |   | executor.py |
     | Campaign   |   | DM Response |
     | Generator  |   | Engine      |
     +--------+---+   +-----+-------+
              |             ▲
              |             |
        +-----v-------------v----+
        |      memory.py         |
        |  Load campaign plan    |
        |  (campaign.json)       |
        +------------------------+
```

- `planner.py`: Generates the full campaign from user prompt using Gemini.
- `memory.py`: Stores the campaign as JSON and is used to provide context to the executor.
- `executor.py`: Receives user actions + campaign context and crafts responses using Gemini.

---

### 3. **Tools / APIs**

- **Google Gemini API (2.5 Flash)**  
  Used for campaign planning and in-game narration via prompt chaining.

---

### 4. **Observability**
- Console logs for FastAPI
- Error handling via structured exception returns
- JSON plan acts as minimal persistent state