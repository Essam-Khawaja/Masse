import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_planner_prompt(setting, party_size, party_level, tone, goal):
    return f"""
    You are a professional tabletop RPG game master. Generate a full 3-act fantasy RPG adventure campaign.

    ## Context
    - Setting: {setting}
    - Party size: {party_size} characters
    - Starting party average level: {party_level}
    - Style/tone: {tone}
    - Campaign goal: {goal}

    ## Party Progression:
    The party starts at level {party_level} and should gain levels progressively across the 3 acts, reaching approximately level {party_level + 2} by the final act.

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
            "type": "beast",
            "challenge_rating": "CR 2",
            "description": "A corrupted forest guardian emerges from the mist to halt their progress.",
            "twist": "The wolf was once a protector of the realm—can it be saved instead of slain?"
        }}
        }},
        ...
    ]
    }}
    """

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=generate_planner_prompt('Post-Apocalyptic', 4, 2, 'heavy', 'save the')
)
print(response.text)