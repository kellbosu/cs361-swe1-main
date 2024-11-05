from user_info import user1

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
    cmd_list = """COMMANDS:
            ENTER: 'about' to learn more about this app.
            ENTER: 'program' to start a new program.
            ENTER: 'update' to change your maxes.
            ENTER: 'stats' to view your current stats.
            ENTER: 'quit' to close the program\n"""
    print(cmd_list)

def update_bench():
    try:
        user1['bench_max'] = int(input("Enter your current bench press max? "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

def update_squat():
    try:
        user1['squat_max'] = int(input("Enter your current squat max? "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

def update_deadlift():
    try:
        user1['deadlift_max'] = int(input("Enter your current deadlift max? "))
    except ValueError:
        print("Silly tinkerer, please enter a valid integer.")

def update_maxes():
    update_bench()
    update_squat()
    update_deadlift()

def program_goals():
    print("""
            What do you want to achieve from you program?
            Enter 1 if: you want to tone up.
            Enter 2 if: you want to get jacked.
            Enter 3 if: you want to strike fear into the hearts of your enemies.
                """)
    chosenProg = input("Choose your program: ").strip().lower()
    if chosenProg == "1":
        user1['current_program'] = 'Skinny Jeans'
        print("            You're on the 'Skinny Jeans' program.")
    elif chosenProg == "2":
        user1['current_program'] = 'Thunder Pump'
        print("            You're on the 'Thunder Pump' program! Vascularity is your middle name.")
    elif chosenProg == "3":
        user1['current_program'] = 'Destructo De Mundos'
        print("            You're on the 'Destructo De Mundos' program! Say your prayers.")

def view_stats():
    print("\n")
    print(f"            YOUR CURRENT BENCH MAX IS: {user1['bench_max']}.")
    print(f"            YOUR CURRENT SQUAT MAX IS: {user1['squat_max']}.")
    print(f"            YOUR CURRENT DEAD MAX IS:  {user1['deadlift_max']}.")
    print(f"            YOUR CURRENT PROGRAM IS:  {user1['current_program']}.")
    print("\n")

def skinny_jeans():
    None

def thunder_pump():
    None

def destructo():
    None