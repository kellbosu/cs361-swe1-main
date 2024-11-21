import time
import pyfunk
import subprocess
import json

def start_program_service():
    subprocess.run(["python3", "program_service.py"])

def start_login_service():
    # Starts login microservice as a subprocess
    subprocess.run(["python3", "login_service.py"])

def wait_for_login():

    # Poll the JSON file to check if the user successfully logged in
    while True:
        with open("data.json", "r") as file:
            user_data = json.load(file)

        # Check if any user has "auth": "success"
        for user in user_data["users"]:
            if user["auth"] == "success":
                current_user = user["username"]
                user["auth"] = ""
                with open("data.json", "w") as file:
                    json.dump(user_data, file, indent=4)
                    print("Proceeding to main UI.\n")
                return current_user
                # main()
                # break
            else:
                time.sleep(1)

def main(user):
    print("""
    ----------------------------------------------------------------------------
                        WELCOME TO FITNESS TRACKER
    Save your money and ditch the personal trainer. Get stronger with science!
    
    DISCLAIMER: Although money and science are way cooler than personal trainers,
    you should always consult a physician before starting a new fitness program 
    because your bones might explode...
    
    ----------------------------------------------------------------------------
    """)

    active_user = user
    while True:

        pyfunk.commandlist()
        command = input("Enter a command: ").strip().lower()

        # Brings up about page.
        if command == "about":
            pyfunk.about()

        # Begins a new program.  If user has not set maxes, user is prompted to set maxes.
        elif command == "program":
            with open("data.json", "r") as file:
                data = json.load(file)
            for user in data["users"]:
                if user["username"] == active_user and user["bench"] == "":
                    print("We need your maxes before we can make a program.\n")
                    user["bench"] = int(input("Enter your current bench max: "))
                    user["squat"] = int(input("Enter your current squat max: "))
                    user["deadlift"] = int(input("Enter your current deadlift max: "))
                    user["program"] = "start new"
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    start_program_service()

                elif user["username"] == active_user:
                    # if user["program"] != "":
                    #     start_program_service()
                    # else:
                    user["program"] = "start new"
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    start_program_service()

        # Prompts the user to enter new maxes.
        elif command == "update":
            pyfunk.update_maxes(active_user)

        elif command == "stats":
            time.sleep(1)
            pyfunk.view_stats(active_user)

        # Quits the program.
        elif command == "quit":
            print("Have a great workout! Goodbye!")
            time.sleep(1)
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    # Initiates login microservice as subprocess
    start_login_service()

    # Successful user login credential assigned to var
    current_user = wait_for_login()
    print("Loading. Please wait...\n")
    time.sleep(1)
    print(f"\nHello, {current_user}")
    time.sleep(1)

    # Hands current user info to main
    main(current_user)





