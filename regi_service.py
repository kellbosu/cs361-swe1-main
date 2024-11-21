import time
import json

print("""\n
                WELCOME TO THE REGISTRATION SCREEN\n
    """)
print("""COMMANDS:
            ENTER: Desired username and password to crate account.            
            ENTER: '/' as username to go back to login.
""")
time.sleep(1)

# Loads data to check and register user
def load_data():
    try:
        with open("data.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}


# METHOD COMPLETE: SAVES DATA
def save_data(data):
    with open("data.json", 'w') as file:
        json.dump(data, file, indent=4)


# Used for creating unique usernames
def create_username():
    data = load_data()
    username = input("Enter a unique username: ").strip().lower()
    for user in data["users"]:
        if username == user["username"]:
            print("Username taken. Please choose another.\n")
            return create_username()
    return username

# Used for creating passwords
def create_password():
    load_data()
    password = input("Enter a password: ")
    return password


def add_user():
    data = load_data()
    username = create_username()
    if username == "/":
        return
    password = create_password()
    user = {
            "auth": "",
            "username": username,
            "password": password,
            "bench": "",
            "squat": "",
            "deadlift": "",
            "program": "",
            }
    data["users"].append(user)
    save_data(data)
    print("""
Registration Successful!
Moving to login page...
""")
    time.sleep(2)






if __name__ == "__main__":
    add_user()