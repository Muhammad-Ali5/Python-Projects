class Library:
    def __init__(self, book_name):
        self.book = book_name
    
    def availableBook(self):
        with open("library.txt","w") as f:
            f.write("\n:::=>The Books in the library are :::<= \n")
            f.write("=======================================")
            for i, book in enumerate(self.book):
                f.write(f"{i + 1} : {book}\n")
                print(i + 1," : ",book)

    
    def borrowBook(self):
        borrow_book=input("Enter the Book which you want...")
        with open("library.txt","r") as f:
            if borrow_book in self.book:
                print(f"Congratulation the {borrow_book} Book is issued \n Please Return it into 30 days...")
                self.book.remove(borrow_book)
            else:
                print("Sorry this book is not available...")
    
    def returnBook(self):
        return_Book_name=input("Enter the Book name. Which you return : ")
        self.book.append(return_Book_name)
        print(self.book)

    def add_new_book(self):
        add_book=input("Enter the Book name which you want to add...")
        with open("library.txt","a") as f:
            f.write("\nUpdated list ...\n")
            print("====================\n")
            f.write(f"{self.book.append(add_book)}")
            for index, book in enumerate(self.book):
                f.write(f"{index+1}: {book}\n")    

    def exitProgram(self):
        print("Program is successfully terminated...")
        exit(0)

central_library= Library(["python","Djengo","compiler","Html","DataStructure","MachineLearning","Javascript"])
# choice=''
while True:
    print("\n======================================")
    print("::: WELCOME TO CENTRAL LIBRARY :::")
    print("======================================")
    print("Press 1.For display Avaliable Books...")
    print("Press 2.For Borrow Books ...")
    print("Press 3.For Return Books ...")
    print("Press 4.For Add new Books ...")
    print("Press 5.For Exit program ...")
    print("================================")
    choice=eval(input("Enter your choice..."))
    print("================================")
    if choice==1:
        central_library.availableBook()
    elif choice==2:
        central_library.borrowBook()
    elif choice==3:
        central_library.returnBook()
    elif choice==4:
        central_library.add_new_book()
    else:
        central_library.exitProgram()