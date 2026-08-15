from time import sleep 
import random
score = 0
questions_remaining = 0

def cpc_practice_mode():
    easy_questions_dict = {
        "What is 'hello' in French? ": "bonjour",
        "What is 'please' in French? ": "s'il vous plait",
        "What is 'thanks' in French? ": "merci",
        "What is 'you're welcome' in French? ": "de rein",
        "What is 'sorry' in French? ": "pardon",
        "What is 'goodbye' in French? ": "au revoir"
    }

    random_list = []
    for q, a in easy_questions_dict.items():
        random_list.append((q, a))

    random.shuffle(random_list)
    fresh_questions_dict = dict()

    for item in random_list:
        fresh_questions_dict[item[0]] = item[1]

    for q, a in fresh_questions_dict.items():
        sleep(1)
        print()
        questions_remaining += 1
        print(f"{questions_remaining}Q:")

        answer = input(q)

        if answer.lower() == a:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print()
    return score