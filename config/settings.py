import json

def load_profile(mode):
    with open("config/profiles.json") as f:
        profiles = json.load(f)

    return profiles.get(mode, profiles["balenced"])