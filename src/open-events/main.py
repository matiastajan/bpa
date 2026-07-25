from time import sleep 
from opens import easy_q # Computer Programming Concepts, Information Technology Concepts

difficulties = ["easy", "medium", "hard"]

opens = {
    1: "computer programming concepts",
    2: "information technology concepts"
}

modes = {
    "a": "practice mode",
    "b": "simulation mode"
}

def normal_result():
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%")
    sleep(3)
    print("Goodbye!")
    quit()

def expert_result():
    print(f"You got {score} questions correct! ({str((score / total_questions) * 100)}%)")
    sleep(2)
    print("Goobye!")
    quit()

def get_open():
    pass

def get_difficulty():
    while True:
        difficulty = input("Type the difficulty of your quiz Easy/Medium/Hard: ").lower()
        if difficulty in difficulties:
            sleep(1)
            break
        else:
            print("Not a valid difficulty.")
            sleep(6.7)

    return difficulty

def get_mode():
    while True:
        mode = input('Type "a" for pratice mode, or type "b" for simulation mode (otherwise "?" for more info): ').lower()
        if mode in modes.keys():
            print(f"Mode selected: {modes.items.capitalized()}")
            break
        elif mode == "?":
            print("\nPractice Mode: After answering each question, it TELLS you whenever your answer was correct or incorrect at the moment. Prompts ALL (50+) of the questions that open contains.")
            print("Simulation Mode: After answering each question, it DOESN'T TELL you whenever your answer was correct or incorrect UNTIL the end. Prompts and selects ONLY 50 questions the open contains.\n")
            sleep(4)
            continue
        else:
            print("Not a valid answer, please try again.")
            sleep(0.5)
    
    return mode

def main():
    print("Welcome to French Quiz!")

    playing = input("Do you want to play (Yes/No)? ")
    if playing.lower() != "yes":
        quit()

    print("Okay, lets begin! :)")
    print()
    sleep(1)

    difficulty = get_difficulty()
    # open = get_open()
    mode = get_mode()

    if difficulty == "easy":
        total_questions = 6
        if mode == "normal":
            score = easy_q.normal_questions()
            normal_result()
        else:
            score = easy_q.random_questions()
            expert_result()

    elif difficulty == "medium":
        total_questions = 8
        if mode == "normal":
            # score = medium_q.normal_questions()
            normal_result()
        else:
            # score = medium_q.random_questions()
            expert_result()

    elif difficulty == "hard":
        total_questions = 10
        if mode == "normal":
            # score = hard_q.normal_questions()
            normal_result()
        else:
            # score = hard_q.random_questions()
            expert_result()

main()