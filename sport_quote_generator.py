import json
import subprocess
import time
import random

def load_data():
    try:
        with open("sport_data.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users: []"}

def save_data(data):
    with open("sport_data.json", 'w') as file:
        json.dump(data, file, indent=4)


def check_for_go():
    data = load_data()
    sport = ""
    team = ""
    fact = ""
    # Checks for the 'go' request to select fact.
    if data["data"]["generate"] == "go":
        # Checks requested parameters for fact.
        sport = data["data"]["sport"]
        team = data["data"]["team"]
    else:
        fr = "Failed request. Please try again."
        return fr
    # If random request, selects random sport.
    if sport == "random":
        sport = random.choice(list(data["sport"].keys()))
    else:
        pass
    # If random request, selects random team.
    if team == "random":
        team = random.choice(list(data["sport"][sport]["teams"].keys()))
    # Finally, uses parameters to select a random sport fact.
    fact = random.choice(data["sport"][sport]["teams"][team])

    # print(sport)
    # print(team)
    # print(fact)
    data["data"]["sport"] = sport
    data["data"]["team"] = team
    data["data"]["fact"] = fact
    data["data"]["generate"] = "complete"
    save_data(data)


if __name__ == "__main__":
    check_for_go()