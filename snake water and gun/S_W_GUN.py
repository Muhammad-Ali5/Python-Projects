import random

def gameWin(comp, you ):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True    
    
print("Computer turn : Snake(s), Water(w), Gun(g) ?")
randomNumber=random.randint(1 , 3)
print(randomNumber)
if randomNumber==1:
    computer="s"
elif randomNumber==2:
    computer="w"
elif randomNumber==3:
    computer="g"

you=input("Your turn : Snake(s), Water(w), Gun(g) ?")

print(f"Computer choose {computer}")
print(f"You choose {you}")

# def main():
res=gameWin(computer, you )
if res==None:
    print("The game is tie!")
elif res:
    print("You win!")
else:
    print("You lose!")