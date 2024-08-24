import random

def gameWin(comp , you):
    if (comp==you):
        return None
    elif(comp=='r'):
        if(you=='p'):
            return True
        elif(you=='s'):
            return False
    elif(comp=='p'):
        if(you=="s"):
            return True
        elif(you=='r'):
            return False
    elif(comp=="s"):
        if(you=="r"):
            return True
        elif(you=='p'):
            return False

print("Computer turn : Rock(r) Paper(p) ,and Scissor(s)?")
randomNumber=random.randint(1 , 3)
if(randomNumber==1):
    computer='r'
elif(randomNumber==2):
    computer='p'
elif(randomNumber==3):
    computer='s'

print("Your turn : Rock(r) Paper(p) ,and Scissor(s)?")
you = input("Enter Your's turn : ")
print("---------------------------")
print(f"Computer choose {computer}")
print(f"You choose {you}")
print("---------------------------")
result=gameWin(computer,you)

if result is None:
    print("The game is tie !")
elif(result==True):
    print("You win the game...")
elif(result==False):
    print("You lose the game!")
