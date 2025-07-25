import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_executor_prompt(campaign_title, act_number, sub_task_type, sub_task_description, party_level, party_size):
    return f"""
    You are an expert Dungeon Master crafting immersive and balanced content for a tabletop RPG campaign.

    Campaign Title: {campaign_title}
    Current Act: {act_number}
    Party Size: {party_size}
    Party Level: {party_level}

    Your task: Generate a detailed {sub_task_type} based on the following description:

    {sub_task_description}

    Make sure the content is engaging, balanced for the party level, and fits within the tone of classic fantasy adventure.

    Please provide your response in clear, descriptive paragraphs suitable for narrating to players.
    """

def execute_subtask_with_history(campaign_title, subtask, history_summary):
    prompt = f"""
    Campaign so far: {history_summary}

    {generate_executor_prompt(
        campaign_title=campaign_title,
        act_number=subtask['act'],
        sub_task_type=subtask['task_type'],
        sub_task_description=subtask['description'],
        party_level=subtask['party_level'],
        party_size=subtask['party_size']
    )}
    """
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response