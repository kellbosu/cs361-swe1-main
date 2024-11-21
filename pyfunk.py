import json
import time


def about():
    print("""
            ABOUT:

            Personal trainers are too dagum expensive.  I wrote this program to help young
            padawans chase the gain train by generating programs based off of 1 rep max percentages
            in the big 3 strength movements: Bench, Squat, and Deadlift. 
            You can enter your maxes in each lift, then generate a tailor made strength program.
            When you quit the program, all data will be cleared.  I plan to update the code so 
            that user's are able to store their data for later retrieval. 

                 """)

def commandlist():
    cmd_list = """\nCOMMANDS:
            ENTER: 'about' to learn more about this app.
            ENTER: 'program' to start a new program.
            ENTER: 'update' to change your maxes.
            ENTER: 'stats' to view your current stats.
            ENTER: 'quit' to close the program\n"""
    print(cmd_list)

# Used to gain bench max
def update_bench(user):
    try:
        user['bench'] = int(input("Enter your current bench max: "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

# Used to gain squat max
def update_squat(user):
    try:
        user['squat'] = int(input("Enter your current squat max: "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

# Used to gain deadlift max
def update_deadlift(user):
    try:
        user['deadlift'] = int(input("Enter your current deadlift max: "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

# Finds active user in data.json, and updates max lifts
def update_maxes(active_user):
    with open('data.json', 'r') as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == active_user:
                update_bench(user)
                update_squat(user)
                update_deadlift(user)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)


def view_stats(active_user):

    with open('data.json', 'r') as file:
        data = json.load(file)

        for user in data["users"]:
            if user["username"] == active_user:
                bench_stat = user["bench"]
                squat_stat = user["squat"]
                deadlift_stat = user["deadlift"]
                program_stat = user["program"]
                print(f"""
            {active_user} STATS:\n
            YOUR CURRENT BENCH MAX IS: {bench_stat}.
            YOUR CURRENT SQUAT MAX IS: {squat_stat}.
            YOUR CURRENT DEAD MAX IS:  {deadlift_stat}.
            YOUR CURRENT PROGRAM IS:  {program_stat}.\n
                """)
                time.sleep(1)

