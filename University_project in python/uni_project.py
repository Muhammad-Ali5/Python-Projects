class Admission:
    def getInfo(self):
        self.name=input("Enter your name : ")
        self.cnic=int(input("Enter your CNIC number : "))
        # if self.cnic==13:
        self.date=input("Enter date : ")
    def dispalyInfo(self):
        print("=================================")
        print(f"    ** NAME : {self.name}")
        print(f"    ** CNIC : {self.cnic}")
        print(f"    ** DATE : {self.date}")
        print("=================================")

class Engeneering(Admission):
    def __init__(self, program):
        self.program=program
    def show_program(self):
        print("\n::: Program in the University :::")
        print("=================================")
        for index, item in enumerate(self.program):
            print(f"{index+1} : {item}")
    def select_Program(self):
        print("------------------------------")
        self.apply=input("Enter the Program : ")
        print("------------------------------")
        if self.apply in self.program:
            print(f"YOu are apply for {self.apply}")
        else:
            print(f"Sorry! jani this program {self.apply} is not available here \n Please apply to other university")
            exit()

    def ShowDepartment(self):
        print(f"       * Congrajulation! {self.name} is salected in the {self.apply} program")

class non_Engineering(Admission):
    def __init__(self, program):
        self.program=program
    
    def show_Program(self):
        print("\n::: Program in the University :::")
        print("=================================")
        for index, item in enumerate(self.program):
            print(f"{index+1}: {item}")
    
    def select_Program(self):
        print("------------------------------")
        self.apply=input("Enter the program name : ")
        print("------------------------------")
        if self.apply in self.program:
            print(f"You apply for {self.apply}")
        else:
            print(f"Sorry jani ! this {self.apply}program is not available here. \n Please apply to other university")
            exit()

    def ShowDepartment(self):
        print(f"       * Congrajulation! {self.name} is salected in the {self.apply} program")

a1=Admission()
E_std=Engeneering(["Civil Engineering",
    "Mechanical Engineering",
    "Electrical Engineering",
    "Computer Engineering",
    "Chemical Engineering",
    "Aerospace Engineering",
    "Biomedical Engineering",
    "Industrial Engineering",
    "Environmental Engineering",
    "Materials Engineering"])
NE_std = non_Engineering(["Computer Science",
    "Bs-English",
    "Artificial Intelligence",
    "Data Science"])
while True:
    print("\n::) WELCOME TO UET MARDAN ::)")
    print("=============================")
    welcome='''\tPress 1. Engineering Departements
        Press 2. Non Engineering Departements
        Press 3. Exit '''
    print(welcome)
    print("\t=================================")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        E_std.getInfo()
        E_std.dispalyInfo()
        E_std.show_program()
        E_std.select_Program()
        E_std.ShowDepartment()
    elif choice==2:
        NE_std.getInfo()
        NE_std.dispalyInfo()
        NE_std.show_Program()
        NE_std.select_Program()
        NE_std.ShowDepartment()
    else:
        print("You are successfully terminated...")
        exit()
    
