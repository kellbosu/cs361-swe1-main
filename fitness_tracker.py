import time
import pyfunk
from user_info import user1

def main():
    print(""" 
                        WELCOME TO FITNESS TRACKER
    Save your money and ditch the personal trainer. Get stronger with science!
    
    DISCLAIMER: Although money and science are way cooler than personal trainers,
    you should always consult a physician before starting a new fitness program 
    because your bones might explode...
    """)

    while True:

        pyfunk.commandlist()
        command = input("Enter a command: ").strip().lower()

        # Brings up about page.
        if command == "about":
            pyfunk.about()
        # Begins a new program.  If user has not set maxes, user is prompted to set maxes.

        elif command == "program":
            if user1['bench_max'] == 0 and user1['squat_max'] == 0 and user1['deadlift_max'] == 0:
                print("Before we get started, what are your current maxes?")
                pyfunk.update_bench()
                pyfunk.update_squat()
                pyfunk.update_deadlift()
            # Asks users what their goals are to determine the right program.
            pyfunk.program_goals()

        # Prompts the user to enter new maxes.
        elif command == "update":
            pyfunk.update_maxes()

        elif command == "stats":
            pyfunk.view_stats()

        # Quits the program.
        elif command == "quit":
            print("Have a great workout! Goodbye!")
            time.sleep(1)
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

