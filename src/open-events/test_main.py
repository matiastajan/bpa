from time import sleep
from opens import easy_q # Computer Programming Concepts, Information Technology Concepts

modes = ["normal", "expert"] # Will be replaced by the new modes dict

difficulties = { # Will be replaced by the "opens" dict
    1: "easy",
    2: "medium",
    3: "hard"
}

modes_dict = {
    1: "normal",
    2: "expert"
}

opens = {
    1: "computer programming concepts",
    2: "information technology concepts"
}

# modes = {
#     "a": "practice mode",
#     "b": "simulation mode"
# }

def loop_difficulties():
    for key, value in difficulties.items():
        print(f"{key}: {value.title()}")
        sleep(0.25)

def loop_modes():
    for key, value in modes_dict.items():
        print(f"{key}: {value.title()}")
        sleep(0.25)

def normal_result(score, total_questions):
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%")
    sleep(3)
    print("Goodbye!")
    quit()

def expert_result(score, total_questions):
    print(f"You got {score} questions correct! ({str((score / total_questions) * 100)}%)")
    sleep(2)
    print("Goobye!")
    quit()

def get_difficulty():
    while True:
        loop_difficulties()
        difficulty = input("Type the difficulty number (#) for your quiz: ")
        if difficulty.isdigit():
            difficulty = int(difficulty)
            if difficulty in difficulties:
                print(f"Great! Difficulty chosen: {difficulties[difficulty].title()}\n")
                sleep(1)
                break
            else:
                print("Please enter a valid number that corresponds to the difficulty.\n")
        else:
            print("Please enter the difficulty number (#) next time.\n")
                       
    return difficulty

def get_mode():
    while True:
        mode = input("Type the mode for your difficulty Normal/Expert or ? for info: ").lower()
        if mode in modes:
            break
        elif mode == "?":
            print()
            print("Normal: questions are organiazed by default in a orden & tells you the correct answer.")
            print("Expert: questions are random & it does not tell you the correct answer.")
            print()
            sleep(4)
            continue
        else:
            print("Not a valid mode.")
            sleep(0.5)

    return mode

def get_mode_dict():
    while True:
        loop_modes()
        mode = input("Type the mode number (#) for your quiz (or ? for more information): ")
        if mode.isdigit():
            mode = int(mode)
            if mode in modes_dict:
                print(f"Terrific! Mode chosen: {modes_dict[mode].title()}\n")
                sleep(1)
                break
            else:
                print("Please enter a valid mode number (#) next time.")
        elif mode == "?":
            print("\nNormal: questions are organiazed by default in a orden & tells you the correct answer.")
            print("Expert: questions are random & it does not tell you the correct answer.\n")
            sleep(4)
        else:
            print("Please enter a mode number or '?' for information.")

    return mode

def main():
    print("Welcome to French Quiz! (Mastered Version)")

    playing = input("Do you want to play (Yes/No)? ")
    if playing.lower() != "yes":
        quit()

    print("Okay, lets begin! :)\n")
    sleep(1)

    difficulty = get_difficulty()
    # mode = get_mode()
    mode = get_mode_dict()

    if difficulty == 1: # Easy
    # total_questions = 6
        if mode == 1:
            sleep(1)
            score = easy_q.normal_questions(0, 0)
            normal_result(score, 6)
        elif mode == 2:
            sleep(1)
            score = easy_q.random_questions(0, 0)
            expert_result(score, 6)

main()

# elif difficulty == "medium":
#     total_questions = 8
#     if mode == "normal":
#         score = medium_q.normal_questions()
#         normal_result()
#     else:
#         score = medium_q.random_questions()
#         expert_result()

# elif difficulty == "hard":
#     total_questions = 10
#     if mode == "normal":
#         score = hard_q.normal_questions()
#         normal_result()
#     else:
#         score = hard_q.random_questions()
#         expert_result()