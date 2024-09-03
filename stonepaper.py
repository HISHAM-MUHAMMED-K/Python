import random
def get_userchoice():
    userchoice=input("enter 'rock','paper','scissor'")
    while userchoice not in ['rock','paper','scissor']:
        print('invalid option please re enter')
        userchoice=input("enter'rock','paper','scissor'")
    return userchoice
def get_computerchoice():
    return random.choice(['rock','paper','scissor'])

def determine_winner(user,computer):
    if (user==computer):
        print("tie")
    elif (user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="paper" and computer=="rock"):
        print("user won")
    else:
            print("computer won") 
def game():
    a=get_userchoice()
    b=get_computerchoice() 
    print(a,b) 
    result=determine_winner(a,b) 
    print(result)            
game()


