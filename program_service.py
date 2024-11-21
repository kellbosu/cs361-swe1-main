import json
import time

import pandas as pd


def get_user():

    with open("data.json", "r") as file:
        data = json.load(file)
    for user in data["users"]:
        if user["program"] == "start new":
            current_user = user["username"]
            print(f"Hello {user["username"]}, let's get juicy!\n")
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            return current_user

# Used to identify what kind of program user wants to pursue
def set_program(user):
    with open("data.json", "r") as file:
        data = json.load(file)
    for name in data["users"]:
        if name["username"] == user:
            if name["program"] == "start new":
                print("""
            What do you want to achieve from you program?\n
            Enter 1 if: you want to tone up.
            Enter 2 if: you want to get jacked.
            Enter 3 if: you want to strike fear into the hearts of your enemies.
                                """)
                while True:
                    chosen_prog = input("Choose your program: ").strip().lower()
                    if chosen_prog == "1":
                        name["program"] = "Skinny Jeans"
                        print("\n")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                            break

                    elif chosen_prog == "2":
                        name["program"] = "Thunder Pump"
                        print("\n")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                            break

                    elif chosen_prog == "3":
                        name["program"] = "Destructo De Mundos"
                        print("\n")
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                        break
                    elif chosen_prog == "/":
                        break
                    else:
                        print("Incorrect selection. Try again.")


# Used to create a new program
def make_program(user):
    time.sleep(1)
    with open("data.json", "r") as file:
        data = json.load(file)
    for name in data["users"]:
        if name["username"] == user:
            if name["program"] == "Skinny Jeans":
                bench = name["bench"]
                squat = name["squat"]
                deadlift = name["deadlift"]

                program = {
                    "Wk 1": {
                        "Bench Day": f"3 x 10 reps @ {round(bench * 0.6)} lbs|",
                        "Squat Day": f"3 x 10 reps @ {round(squat * 0.6)} lbs|",
                        "Dead Day": f"3 x 10 reps @ {round(deadlift * 0.6)} lbs|"
                    },
                    "Wk 2": {
                        "Bench Day": f"5 x 5 reps @ {round(bench * 0.7)} lbs|",
                        "Squat Day": f"5 x 5 reps @ {round(squat * 0.7)} lbs|",
                        "Dead Day": f"5 x 5 reps @ {round(deadlift * 0.7)} lbs|"
                    },
                    "Wk 3": {
                        "Bench Day": f"10 x 3 reps @ {round(bench * 0.75)} lbs|",
                        "Squat Day": f"10 x 3 reps @ {round(bench * 0.75)} lbs|",
                        "Dead Day": f"10 x 3 reps @ {round(bench * 0.75)} lbs|",
                    },
                    "Wk 4": {
                        "Bench Day": "Rest |",
                        "Squat Day": "Rest |",
                        "Dead Day": "Rest |"
                    },
                }
                print("            You're on the Skinny Jeans program!")
                pd.set_option('display.max_columns', None)
                df = pd.DataFrame(program)
                print(df)

            elif name["program"] == "Thunder Pump":
                bench = name["bench"]
                squat = name["squat"]
                deadlift = name["deadlift"]

                program = {
                    "Wk 1": {
                          "Bench Day": f"3 x 10 reps @ {round(bench * 0.65)} lbs|",
                          "Squat Day": f"3 x 10 reps @ {round(squat * 0.65)} lbs|",
                          "Dead Day": f"3 x 10 reps @ {round(deadlift * 0.65)} lbs|"
                    },
                    "Wk 2": {
                          "Bench Day": f"5 x 5 reps @ {round(bench * 0.75)} lbs|",
                          "Squat Day": f"5 x 5 reps @ {round(squat * 0.75)} lbs|",
                          "Dead Day": f"5 x 5 reps @ {round(deadlift * 0.75)} lbs|"
                    },
                    "Wk 3": {
                          "Bench Day": f"10 x 3 reps @ {round(bench * 0.8)} lbs|",
                          "Squat Day": f"10 x 3 reps @ {round(bench * 0.8)} lbs|",
                          "Dead Day": f"10 x 3 reps @ {round(bench * 0.8)} lbs|",
                    },
                    "Wk 4": {
                          "Bench Day": "Rest |",
                          "Squat Day": "Rest |",
                          "Dead Day": "Rest |"
                    },
                }
                print("            You're on the Thunder Pump program!")
                pd.set_option('display.max_columns', None)
                df = pd.DataFrame(program)
                print(df)

            elif name["program"] == "Destructo De Mundos":
                bench = name["bench"]
                squat = name["squat"]
                deadlift = name["deadlift"]

                program = {
                    "Wk 1": {
                          "Bench Day": f"3 x 10 reps @ {round(bench * 0.7)} lbs |",
                          "Squat Day": f"3 x 10 reps @ {round(squat * 0.7)} |",
                          "Dead Day": f"3 x 10 reps @ {round(deadlift * 0.7)} |"
                    },
                    "Wk 2": {
                          "Bench Day": f"5 x 5 reps @ {round(bench * 0.75)} lbs|",
                          "Squat Day": f"5 x 5 reps @ {round(squat * 0.75)} lbs|",
                          "Dead Day": f"5 x 5 reps @ {round(deadlift * 0.75)} lbs|"
                    },
                    "Wk 3": {
                          "Bench Day": f"10 x 3 reps @ {round(bench * 0.85)} lbs|",
                          "Squat Day": f"10 x 3 reps @ {round(bench * 0.85)} lbs|",
                          "Dead Day": f"10 x 3 reps @ {round(bench * 0.85)} lbs|",
                    },
                    "Wk 4": {
                          "Bench Day": "Rest |",
                          "Squat Day": "Rest |",
                          "Dead Day": "Rest |"
                    },
                }
                print("            You're on the Destructo De Mundos program!!")
                pd.set_option('display.max_columns', None)
                df = pd.DataFrame(program)
                print(df)
            else:
                print("Program not found. Please create a new program.\n")




if __name__ == "__main__":

    user = get_user()
    # set_program(user)
    # make_program(user)

    while True:
        print("""COMMANDS:
             ENTER: 'new' to start a new program.
             ENTER: '/' to go back to the main screen.
        """)
        command = input("Enter a command: ")
        if command == 'new':
            verify = (input("""
            Are you sure you're ready for a new program??
            (Y/N)?\n
Enter a command: """)).lower().strip()
            if verify == "y":
                with open("data.json", "r") as file:
                    data = json.load(file)
                for name in data["users"]:
                    if name["username"] == user:
                        name["program"] = "start new"
                        with open("data.json", "w") as file:
                            json.dump(data, file, indent=4)
                set_program(user)
                make_program(user)
            elif verify == "n":
                break
        elif command == '/':
            break
        else:
            print("Invalid command. Enter a correct COMMAND")
#
#






