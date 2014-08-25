def ask (question):
    print(question)
    answer = input().strip()
    return answer


###############################################################
print("Welcome")



name1  = ask("What is your name?").title()
name2  = ask("What is your friends name?").title()
age1 = int(ask("What is your age?"))
age2 = int(ask("What is your friends age?"))


years_apart = abs(age1 - age2)

print('{} and {} are {} years_apart.'.format(name1,name2,years_apart))



    
