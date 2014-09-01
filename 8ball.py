import random

answers = [
    'yes','no','maybe']


while True:
    print("whats is your question")
    question = input('>')


    answer = random.choice(answers)
    print(answer)


