def ask (question):
    print(question)
    answer = input().strip()
    return answer


##########################################################
print("Welcome to the age differens thing a magiger")



name1  = ask("What is your name?").title()
name2  = ask("What is your friends name?").title()
age1 = int(ask("What is your age?"))
age2 = int(ask("What is your friends age?"))


years_apart = abs(age1 - age2)

print('{} and {} are {} years_apart.'.format(name1,name2,years_apart))     


days_in_year = 365.242
days_apart = years_apart * days_in_year


print("you are " + str (days_apart) + " days apart.")






    
