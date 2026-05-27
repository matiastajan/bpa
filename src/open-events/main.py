import time as t
from questions import easy_q # Computer Programming Concepts, Information Technology Concepts

difficulties = ["easy", "medium", "hard"]
modes = ["normal", "expert"]

def normal_result():
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%")
    t.sleep(3)
    print("Goodbye!")
    quit()

def expert_result():
    print(f"You got {score} questions correct! ({str((score / total_questions) * 100)}%)")
    t.sleep(2)
    print("Goobye!")
    quit()
    
print("Welcome to French Quiz! (Mastered Version)")
t.sleep(1.5)

playing = input("Do you want to play (Yes/No)? ")
if playing.lower() != "yes":
    quit()

print("Okay, lets begin! :)")
print()
t.sleep(1)

# get difficulty
while True:
    difficulty = input("Type the difficulty of your quiz Easy/Medium/Hard: ").lower()
    if difficulty in difficulties:
        t.sleep(1)
        break
    else:
        print("Not a valid difficulty.")
        t.sleep(0.5)

# get mode
while True:
    mode = input("Type the mode for your difficulty Normal/Expert or ? for info: ").lower()
    if mode in modes:
        break
    elif mode == "?":
        print()
        print("Normal: questions are organiazed by default in a orden & tells you the correct answer.")
        print("Expert: questions are random & it does not tell you the correct answer.")
        print()
        t.sleep(4)
        continue
    else:
        print("Not a valid mode.")
        t.sleep(0.5)

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