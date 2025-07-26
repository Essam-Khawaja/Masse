from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # Used to generate type validation
from fastapi.middleware.cors import CORSMiddleware  # Need to use CORS for NextJS frontend framework
import uvicorn  # To run the API locally
from typing import List # A type for the schemas

from planner import planner_executor, check_prompt
from executor import get_user_text, elaborate_campaign

from memory import save_plan_to_file, load_plan_from_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Making the Campaign Request Type
class Battle(BaseModel):
    enemy: str
    enemy_type: str
    challenge_rating: str
    description: str
    twist: str

class Act(BaseModel):
    title: str
    summary: str
    locations: List[str]
    battle: Battle

class CampaignPlan(BaseModel):
    acts: List[Act]

class CampaignRequest(BaseModel):
    message: str



# Below are all the paths to the API:
@app.get("/test")
def root():
    return {'message': 'AI Dungeon Master is RUNNING LETS GOOO!'}

@app.post("/generate-campaign")
async def generate_campaign(req: CampaignRequest):
    try:
        checkPrompt = check_prompt(req.message)
        print(checkPrompt)
        if checkPrompt.lower() == 'yes':
            plan = planner_executor(
                req.message
            )
            save_plan_to_file(plan)
            reply = get_user_text(plan)
            return {"reply": reply}
        else: 
            return {"reply": checkPrompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate plan: {e}")
    
@app.post("/elaborate-campaign")
async def elaborate_campaign_route(req: CampaignRequest):
    try:
        response = elaborate_campaign(req.message)
        return {"reply": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate plan: {e}")
