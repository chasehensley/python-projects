def ask(question):
    answer=input(question)
    anser=answer.strip().lower()
    print("thou hast answered:{}".format(answer))
    return answer
    

def let_pass():
    print("Fine. Off you go then.")


def kill():
     print("thou art cast into the gorge.")

     
###################################################################


name=ask("What is your name?")
quest=ask("What is your quest?")

if name == 'lancelot':
    color = ask("What is your favoite color? ")
    if color == 'blue':
        let_pass()
    else:
        kill ()
    
