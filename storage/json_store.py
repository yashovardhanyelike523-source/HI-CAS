import json

def save_inventory(data):
    with open("inventory.json", "w") as f:
        json.dump([item.to_dict() for item in data], f, indent=4)

def load_inventory():
    try:
        with open("inventory.json") as f:
            return json.load(f)
    except:
        return []