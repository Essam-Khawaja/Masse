import os
from dotenv import load_dotenv
from google import genai
import json
import re

from memory import load_plan_from_file

load_dotenv()

def check_prompt(userInput):
    context = load_plan_from_file()
    prompt = f"""
    You are a professional tabletop RPG game master.
    Here is the context from previous prompts:
    {context}
    
    Check whether this prompt is legible or is in the right mind for helping out dungeon masters:
    {userInput}
    Be easygoing, try and just let it pass. If dungeons and dragons is mentioned, then its an automatic pass. Just be easy on the user, no need to try too hard.
    If prompt makes sense, reply with a 'yes', otherwise respond with a text response to the user.
    """
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def generate_planner_prompt(userInput):
    return f"""
    You are a professional tabletop RPG game master. Generate a full 3-act fantasy RPG adventure campaign.

    ## Here is some context provided by the user:
    {userInput}

    Make sure to include party level progression as you continue.

    ## Output Structure:
    Respond in valid JSON format like the structure below. Each act should contain:
    - A short narrative summary (2–4 sentences)
    - 2–3 key locations or events
    - At least 1 major **battle encounter** per act, with:
    - Enemy name and type
    - Challenge rating (CR) balanced to party level for that act
    - Challenge description
    - Unique twist (e.g., timed battle, moral dilemma, magic gone wrong)

    ## Example Format:
    ```json
    {{
    "acts": [
        {{
        "title": "Act I: The Whispering Forest",
        "summary": "The party begins their journey by investigating strange disappearances in the woods...",
        "locations": ["Village of Gladehaven", "Whispering Forest", "Ancient Tree of Echoes"],
        "battle": {{
            "enemy": "Shadowfang Wolf",
            "enemy_type": "beast",
            "challenge_rating": "CR 2",
            "description": "A corrupted forest guardian emerges from the mist to halt their progress.",
            "twist": "The wolf was once a protector of the realm—can it be saved instead of slain?"
        }}
        }},
        ...
    ]
    }}
    """

def planner_executor(userInput):
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=generate_planner_prompt(userInput)
    )
    # Extract JSON inside the triple backticks
    match = re.search(r'```json\s*(\{.*\})\s*```', response.text, re.DOTALL)
    if not match:
        raise ValueError("Could not extract JSON from response")

    json_str = match.group(1)

    try:
        parsed_data = json.loads(json_str)
        return parsed_data 
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")