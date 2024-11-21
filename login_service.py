import json
import time
import subprocess


def new_registration():
    # Start the login microservice as a subprocess
    subprocess.run(["python3", "regi_service.py"])  # Adjust command as needed
    director()


# Asks for a command to either login or register new user
def director():
    print("""\n
                WELCOME TO THE LOGIN SCREEN
    """)
    while True:
        login_commands()
        command = input("Enter a command: ").strip().lower()
        if command == "login":
            print("""COMMANDS:
            ENTER: Username and password to proceed.
            ENTER: '/' to perform a different command.
            """)
            verify_login()
            break

        elif command == "register":
            print("Moving to registration page...\n")
            time.sleep(1)
            new_registration()
            break

        elif command == "quit":
            print("Goodbye!")
            time.sleep(1)
            break
        else:
            print("Unknown command. Please try again.")

# Prints commands to use on director(), determines if login, register new user, or quits
def login_commands():
    time.sleep(1)
    cmds = """COMMANDS:
            ENTER: 'login' to login to your account.
            ENTER: 'register' to create a new account.
            ENTER: 'quit' to close the program.
    """
    print(cmds)

# Checks login info in JSON file, then updates authentication status to 'success' or 'fail'
def verify_login():
    while True:
    # Load user data from JSON file
        with open("data.json", "r") as file:
            user_data = json.load(file)

        # Prompt for credentials & initialized login status
        username = input("Enter username: ").strip().lower()
        if username == '/':
            director()
            break

        password = input("Enter password: ")
        if password == '/':
            director()
            break


        login_success = False
        # Verify credentials. Sets 'success' or 'fail' status.
        for user in user_data["users"]:
            if username == user["username"] and password == user["password"]:
                user["auth"] = "success"
                login_success = True
                with open("data.json", "w") as file:
                    json.dump(user_data, file, indent=4)
                    print("\nSuccessful login!")
                    break
        # If login fails, tries again.
        if login_success:
            break
        else:
            print("\nfailed login... Try again.")


if __name__ == "__main__":
    director()

