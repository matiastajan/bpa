from time import sleep
from opens import easy_q # Computer Programming Concepts, Information Technology Concepts

difficulties = { # Will be replaced by the "opens" dict
    1: "easy",
    2: "medium",
    3: "hard"
}

modes = { # Will be replaced by the new modes dict
    1: "normal",
    2: "expert"
}

opens = {
    1: "computer programming concepts",
    2: "information technology concepts"
}

modes_for_opens = {
    "a": "practice mode",
    "b": "simulation mode"
}

def loop_difficulties():
    for key, value in difficulties.items():
        print(f"{key}: {value.title()}")
        sleep(0.25)

# def loop_modes():
#     for key, value in modes.items():
#         print(f"{key}: {value.title()}")
#         sleep(0.25)

def loop_modes():
    for key, value in modes_for_opens.items():
        print(f"{key.title()}: {value.title()}")
        sleep(0.25)

def show_result(score, total_questions):
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%")
    sleep(2)
    print("Goodbye!")
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

# def get_mode():
#     while True:
#         loop_modes()
#         mode = input("Type the mode number (#) for your quiz (or ? for more information): ")
#         if mode.isdigit():
#             mode = int(mode)
#             if mode in modes:
#                 print(f"Terrific! Mode chosen: {modes[mode].title()}\n")
#                 sleep(1)
#                 break
#             else:
#                 print("Please enter a valid mode number (#) next time.")
#         elif mode == "?":
#             print("\nNormal: questions are organiazed by default in a orden & tells you the correct answer.")
#             print("Expert: questions are random & it does not tell you the correct answer.\n")
#             sleep(4)
#         else:
#             print("Please enter a mode number or '?' for information.")

#     return mode

def get_mode():
    while True:
        loop_modes()
        mode = input("Type the mode symbol (A or B) for your quiz (otherwise type '?' for more information): ")
        if mode.lower() in modes_for_opens:
            mode = str(mode)
            print(f"Terrific! Mode chosen: {modes_for_opens[mode].title()}\n")
            sleep(1)
            break
        elif mode == "?":
            print("\nPractice Mode: After answering each question, it TELLS you whenever your answer was correct or incorrect at the moment. Prompts ALL (50+) of the questions that open contains.")
            print("Simulation Mode: After answering each question, it DOESN'T TELL you whenever your answer was correct or incorrect UNTIL the end. Prompts and randomly selects ONLY 50 questions the open contains.\n")
            sleep(4)
        else:
            print("Please enter a mode symbol (A or B) or '?' for more information.")

    return mode

def main():
    print("Welcome to French Quiz! (Mastered Version)")

    playing = input("Do you want to play (Yes/No)? ")
    if playing.lower() != "yes":
        quit()

    print("Okay, lets begin! :)\n")
    sleep(1)

    difficulty = get_difficulty()
    mode = get_mode()

    if difficulty == 1: # Easy
    # total_questions = 6
        if mode == modes_for_opens["a"]:
            sleep(1)
            score = easy_q.normal_questions(0, 0)
            show_result(score, 6)
        elif mode == modes_for_opens["b"]:
            sleep(1)
            score = easy_q.random_questions(0, 0)
            show_result(score, 6)

main()