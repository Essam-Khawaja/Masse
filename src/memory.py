import json
def save_plan_to_file(plan_data, filename="campaign_memory.json"):
    with open(filename, "w") as f:
        json.dump(plan_data, f, indent=2)

def load_plan_from_file(filename="campaign_memory.json"):
    with open(filename, "r") as f:
        return json.load(f)