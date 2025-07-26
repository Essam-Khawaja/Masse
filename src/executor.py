import os
from dotenv import load_dotenv
from google import genai

from memory import load_plan_from_file

load_dotenv()


def generate_executor_prompt(plan):
    return f"""
    You are an expert Dungeon Master crafting immersive and balanced content for a tabletop RPG campaign.

    Here is the plan we are going to follow based on three acts:
    {plan}

    I want you to generate a user-friendly, and well typed out explnation of this for the user to understand what is going on.
    Do not use nested bullet points, or any other convulted lists.
    Write it out with emojis and beautiful markdown language.
    """

def get_user_text(plan):
    prompt = generate_executor_prompt(plan)
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def elaborate_campaign(userInput):
    context = load_plan_from_file()
    prompt = f"""
    You are an expert Dungeon Master crafting an immersive and balanced content for a tabletop RPG Campaign.
    Here is the context planned so far: 
    {context}

    Use this context to respond to the user's prompt:
    {userInput}
    I want you to generate a user-friendly, and well typed out explnation of this for the user to understand what is going on.
    Do not use nested bullet points, or any other convulted lists.
    Write it out with emojis and beautiful markdown language.
    """
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
