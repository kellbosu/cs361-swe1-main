import json
import subprocess
import random
import time
import sport_methods as sm

data = sm.load_data()
# data["data"]["sport"] = "basketball"
# sm.save_data(data)


# print(data["data"]["sport"])
# print(data["data"]["team"])

def main():

    while True:
        print("""\nCOMMANDS:
        ENTER: 'random' for a random sport fact.
        ENTER: 'select' to choose a sport or team.
        ENTER: 'quit' to exit.
        """)
        command = input("Enter a command: ").lower()

        if command == 'random':
            sm.random_selection()
        elif command == "select":
            sm.select_filter()
        elif command == 'quit':
            break
        else:
            print("Unknown command. Please try again.")
            time.sleep(1)

        print("\n    Loading. Please wait...\n")
        sm.start_fact_generator()
        fact = sm.wait_for_fact()
        time.sleep(1)
        data = sm.load_data()
        print(f"        Sport: {data["data"]["sport"]}.")
        print(f"        Team: {data["data"]["team"]}")
        print(f"        Fact: {fact}")






if __name__ == "__main__":
    main()

