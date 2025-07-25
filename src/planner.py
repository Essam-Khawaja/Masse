import json
import os
import re
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel

load_dotenv()
configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("models/gemini-1.5-flash")

def plan_study(userInput):
    prompt = f"""
    You are a study planner agent. Create a detailed 3-day study plan for the goal: "{userInput}".
    Each day should have exactly 2 learning tasks.
    Respond ONLY in this format:
    {{
      "Day 1": ["Task 1", "Task 2"],
      "Day 2": ["Task 1", "Task 2"],
      "Day 3": ["Task 1", "Task 2"]
    }}
    """
    response = model.generate_content(prompt)
    text = response.text.strip()

    # If it still returns ```json formatting, clean it up
    if text.startswith("```"):
        text = re.sub(r"```[a-z]*", "", text).strip()
        text = text.replace("```", "").strip()

    return json.loads(text)

if __name__ == "__main__":
    goal = "I want to learn basic Python programming"
    plan = plan_study(goal)
    print(plan)