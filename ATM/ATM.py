c_balance = 30000
password = 1234
def checkBalance():
    global c_balance
    with open ("atm.txt","a") as f:
        f.write(f"Your current Balance is : {c_balance}\n")

def widthrawBalance():
    global c_balance
    with open ("atm.txt","a") as f:
        width_bal=int(input("Enter the widthraw amount : "))
        if(width_bal < c_balance):
            c_balance=c_balance-width_bal
            print("Congratulation you widthraw the money...")
            f.write(f"Widthraw amount is : {width_bal}\n")
            f.write(f"Now Current amount is : {c_balance}\n")
        elif(width_bal > c_balance):
            print(f"Your current is : {c_balance} And")
            print("You have exceeded your current balance!")

def depositeBalance():
    global c_balance
    with open ("atm.txt","a") as f:
        dep_amount=int(input("Enter the Deposited amount : "))
        c_balance=c_balance + dep_amount
        print(f"The {dep_amount} amount is successfuly deposited!")
        f.write(f"Deposited amount is : {dep_amount}\n")
        f.write(f"Now Current Balance is : {c_balance}\n")

def user_information():
    with open("atm.txt","a") as f:
            name=input("Enter Your Name :")
            f.write(f"Name is : {name}\n")

def main():
    with open ("atm.txt","a") as f:
        print("==Welcome To Khyber Bank==")
        f.write("====================================\n")
        password=int(input("Enter your password : "))
        f.write("====================================\n")
        if (password==1234):
            user_information()
        # # with open("atm.txt","a") as f:
        #     name=input("Enter Your Name :")
        #     f.write(f"Name is : {name}\n")
            print("=================================")
            print("=> Press 1. Check Balance     ...")
            print("=> Press 2. Widthraw Balance  ...")
            print("=> Press 3. Deposite Balance  ...")
            print("=================================")
            choice=int(input("==> Enter Your Choice : "))
            
            if (choice==1):
                checkBalance()
            elif(choice==2):
                widthrawBalance()
            elif(choice==3):
                depositeBalance()
        elif(password!=1234):
            print("You entered the wrong password!")
            exit(0)

main()