import random

answers = [
    'yes','no','maybe','pickles','Callie','SHUT UP','computer is shutting down','computer is broken now','you are being log off and never allowed on again','hi','bye',]


while True:
    print("whats is your question")
    question = input('>')


    answer = random.choice(answers)
    print(answer)

