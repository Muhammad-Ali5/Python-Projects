class Hotal:
    def __init__(self,menu, prices):
        self.menu = menu
        self.prices=prices

    def check_Menu(self):
        print("** Lists of Menu **")
        print("===================")
        for index, items in enumerate(self.menu):
            print(index+1 ,".", items)

    def check_Menu_Prices(self):
        print("** Lists of Menu with Price **")
        print("==============================")    
        for index, prices in enumerate(self.prices):
            print(index+1,".",prices)

    def order_Menu(self):
        user_menu=input("Enter your Menu...")
        if user_menu in self.menu:
            print(f"Your odered {user_menu} were successfully accepted...\nPlease Wait for a moment")
        elif user_menu not in self.menu:
            print(f"Your ordered menu {user_menu} is not available...")
            # exit()

    def pay_money(self):
        user_pay_money=int(input("Pay the money..."))
        if user_pay_money>=200:
            print("You Paid the money... \tPlease wait for your order.")
        else:
            print("You Paid less money!")

    def exit_hotal(self):
        print("Program successfully terminated!")
        exit()


h1 = Hotal(["chicken","Chawal","mutton","Daal","Biryani","Lobia","Sabze","kabab"],["chicken Rs.200","Chawal Rs.200","mutton Rs.200","Daal Rs.200","Biryani Rs.200","Lobia Rs.200","Sabze Rs.200","kabab Rs.200"])

while True:
    print("\n\n==> WELCOME TO RIVER VEIW :::)")
    print("================================")
    print("Press 1. For Check Menu Lists :)")
    print("Press 2. For Check Menu Price :)")
    print("Press 3. For Order Menu       :)")
    print("Press 4. For Exit             :)")
    print("================================")
    choice = int(input("Enter Your Choice..."))
    print("--------------------------------")
    if choice==1:
        h1.check_Menu()
    elif choice==2:
        h1.check_Menu_Prices()
    elif choice==3:
        h1.order_Menu()
        h1.pay_money()
    elif choice==4:
        h1.exit_hotal()
    else:
        print("You Entered Invalid Input! \n Please Enterd valid input...")