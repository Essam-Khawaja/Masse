# ⚙️ Technical Explanation

## 1. Agent Workflow

1. **Receive user input** via frontend  
2. **(Optional) Load memory** (initial campaign plan from file)  
3. **Generate plan** using `planner.py` via a Gemini API call (ReAct-style prompt)  
4. **Respond to user input** via `executor.py`, using the plan as context  
5. **Return final output** in rich markdown (emojis, story beats)

---

## 2. Key Modules

- **`planner.py`**  
  Prompts Gemini to generate a 3-act fantasy RPG campaign in structured JSON.  
  Uses pattern-based prompting (titles, summaries, battles).

- **`executor.py`**  
  Takes user input and campaign plan to generate dynamic, narrative-rich responses.  
  Provides turn-by-turn AI Dungeon Master narration.

- **`memory.py`**  
  Saves and loads the campaign plan (`campaign.json`) to retain context.  
  No advanced memory; just one plan per session.

---

## 3. Tool Integration

- **Gemini API**  
  All content generation is powered by `gemini-2.5-flash`.  
  Uses `google.generativeai` library to call `generate_content`.

---

## 4. Observability & Testing

- Errors returned via FastAPI exception logs  
- All campaign plans saved as JSON (`campaign.json`)  
- Debugging is via console logs (can be enhanced with proper logging)

---

## 5. Known Limitations

- No persistent memory of user choices over multiple turns  
- Player actions are handled generatively — no strict game rules  
- No branching logic or undo — it’s a loose, fun narrative tool  
- Error handling assumes valid Gemini JSON responses
