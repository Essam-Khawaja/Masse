import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_executor_prompt(plan):
    return f"""
    You are an expert Dungeon Master crafting immersive and balanced content for a tabletop RPG campaign.

    Here is the plan we are going to follow based on three acts:
    {plan}

    I want you to generate a user-friendly, and well typed out explnantion of this for the user to understand what is going on.
    """

def get_user_text(plan):
    prompt = generate_executor_prompt(plan)
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text