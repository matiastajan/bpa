from time import sleep 
import random

def normal_questions(score, questions_remaining):
    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'hello' in French? ")
    if answer.lower() == "bonjour":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Bonjour")

    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'please' in French? ")
    if answer.lower() == "s'il vous plait":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: š'il vous plaît")

    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'thanks' in French? ")
    if answer.lower() == "merci":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Merci")

    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'you're welcome' in French? ")
    if answer.lower() == "de rein":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: De rein")

    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'sorry' in French? ")
    if answer.lower() == "pardon":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Pardon")

    questions_remaining += 1
    answer = input(f"\n{questions_remaining}Q: What is 'goodbye' in French? ")
    if answer.lower() == "au revoir":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Au revoir\n")

    return score

def random_questions(score, questions_remaining):
    easy_questions_dict = {
        "What is 'Hello' in French? ": ["bonjour", "au revoir", "pardon", "merci"],
        "What is 'please' in French? ": ["s'il vous plaît", "au revoir", "pardon", "merci"],
        "What is 'thanks' in French? ": ["merci", "au revoir", "pardon", "s'il vous plaît"],
        "What is 'you're welcome' in French? ": ["de rien", "bonjour", "pardon", "merci"],
        "What is 'sorry' in French (formal)? ": ["pardon", "au revoir", "de rien", "merci"],
        "What is 'goodbye' in French? ": ["au revoir", "bonjour", "pardon", "merci"]
    }

    random_list = []

    for random_question, random_answer in easy_questions_dict.items():
        random_list.append((random_question, random_answer))

    random.shuffle(random_list)
    fresh_questions_dict = dict()

    for item in random_list:
        fresh_questions_dict[item[0]] = item[1]

    for random_question, random_answer in fresh_questions_dict.items():
        sleep(0.5)

        questions_remaining += 1
        print(f"\n{questions_remaining}Q:")

        correct_answer = random_answer[0] # The first answer is the correct

        answer_choices = random_answer.copy()
        random.shuffle(answer_choices)

        print(random_question)

        print(f"A. {answer_choices[0].capitalize()}")
        print(f"B. {answer_choices[1].capitalize()}")
        print(f"C. {answer_choices[2].capitalize()}")
        print(f"D. {answer_choices[3].capitalize()}")

        answer = input("Your answer: ").lower()

        answer_indexes = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3
        }

        if answer in answer_indexes:
            selected_answer = answer_choices[answer_indexes[answer]]

            if selected_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        else:
            print("Invalid answer. Please enter A, B, C, or D.")

    print()

    return score