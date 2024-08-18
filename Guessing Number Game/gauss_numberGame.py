import random

attempt=1
computerGausse=random.randint(1 , 100)
print("::: WELCOME TO NUMBER GUESSING GAME :::")
print("========================================")
print("Guess the Number Between 1 and 100")
print("========================================")
while attempt:
    yourGauss=int(input("Enter your Gausse : "))
    print("----------------------")
    attempt+=1
    # print(randocmNumber)
    if(yourGauss > computerGausse):
        print("Gausse the lower number : ")
        print("----------------------")
    elif(yourGauss < computerGausse):
        print("Gausse the higher number : ")
        print("----------------------")
    if(yourGauss== computerGausse):
        print(f"You Gausse the number in {attempt} attempts... ")
        print("======================================")
        
        with open("hisocre.txt","r")as f:
            hiscore=int(f.read())
        
        if yourGauss<hiscore:
            with open("hisocre.txt","w")as f:
                f.write(str(yourGauss))
        exit(0)
    