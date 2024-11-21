import json
import random
import subprocess
import time

# Initialize Preferences to None
sport = None
team = None


def load_data():
    try:
        with open("sport_data.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users: []"}

def save_data(data):
    with open("sport_data.json", 'w') as file:
        json.dump(data, file, indent=4)

def select_filter():
    data = load_data()
    choices = ["hockey", "football", "basketball", "baseball", "random"]

    sport = input("""
    Choices: hockey, football, basketball, baseball or random
    Enter a sport: """).lower()
    if sport not in choices:
        print("\n    Select a sport from 'Choices'. Please try again")
        return select_filter()

    team = input("""
    Choices: Your favorite team or random
    Enter a team: """).lower()
    if team == "random":
        pass
    elif team not in list(data["sport"][sport]["teams"].keys()):
        print("\n    Incorrect spelling or team does not exist. Please try again")
        return select_filter()


    data["data"]["sport"] = sport
    data["data"]["team"] = team
    data["data"]["generate"] = "go"

    save_data(data)

def random_selection():
    data = load_data()

    data["data"]["sport"] = "random"
    data["data"]["team"] = "random"
    data["data"]["generate"] = "go"

    save_data(data)


def start_fact_generator():
    subprocess.run(["python3", "sport_quote_generator.py"])


def wait_for_fact():
    # Poll the JSON file to check if the user successfully logged in
    while True:
        with open("sport_data.json", "r") as file:
            data = json.load(file)
        if data["data"]["generate"] == "complete":
            fact = data["data"]["fact"]
            return fact
        else:
            time.sleep(1)


def print_random_sports_fact():
    # Load the sports data from the JSON file
    with open('sport_data.json', 'r') as file:
        sports_data = json.load(file)
    # Select a random sport
    sport = random.choice(list(sports_data["sport"].keys()))
    # Select a random team within the chosen sport
    team = random.choice(list(sports_data["sport"][sport]["teams"].keys()))
    # Select a random fact for the chosen team
    fact = random.choice(sports_data["sport"][sport]["teams"][team])

    # Print the result
    print(f"Sport: {sport.capitalize()}")
    print(f"Team: {team.capitalize()}")
    print(f"Fact: {fact}")


# Example usage
print(wait_for_fact())
