import json
def save_plan_to_file(plan_data, filename="campaign_memory.json"):
    try:
        with open(filename, "w") as f:
            json.dump(plan_data, f, indent=2)
    except:
        pass

def load_plan_from_file(filename="campaign_memory.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return 'No context.'