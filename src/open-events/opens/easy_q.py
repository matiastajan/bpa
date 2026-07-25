# 6/6q normal: done
# 6/6q expert: done
import time as t, random
score = 0
questions_remaining = 0

def normal_questions():
    global score, questions_remaining

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'hello' in French? ")
    if answer.lower() == "bonjour":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Bonjour")

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'please' in French? ")
    if answer.lower() == "s'il vous plait":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: š'il vous plaît")

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'thanks' in French? ")
    if answer.lower() == "merci":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Merci")

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'you're welcome' in French? ")
    if answer.lower() == "de rein":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: De rein")

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'sorry' in French? ")
    if answer.lower() == "pardon":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Pardon")

    t.sleep(1)
    print()
    questions_remaining += 1
    answer = input(f"{questions_remaining}Q: What is 'goodbye' in French? ")
    if answer.lower() == "au revoir":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. It was: Au revoir")

    print()
    return score

def random_questions():
    global score, questions_remaining

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
        t.sleep(1)
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