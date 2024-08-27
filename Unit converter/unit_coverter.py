def Celsius_to_Fahrenheit():
    with open("c_t_f_and_inches_to_cm_viceVersaa.txt",'a')as f:
        celsius=eval(input("Enter the temperature in Celsius : "))
# Now we creates the logic's all one by one 
        fahrenheit = (celsius * 9/5 ) + 32
        f.write("==Coversion of Celsius to Fahrenheit==\n")
        f.write(f"The temperature in Fahrenheit is : {fahrenheit}\n")
        f.write("====================================\n\n")
def Fahrenheit_to_Celsius():
    with open("c_t_f_and_inches_to_cm_viceVersaa.txt",'a')as f:
        fahrenheit=eval(input("Enter the temperature in Fahrenheit : "))
        celsius = (fahrenheit -32 )* 5/9
        f.write("==Coversion of Fahrenheit to celsius==\n")
        f.write(f"The temperature in celsius is : {celsius}\n")
        f.write("====================================\n\n")

def Inches_to_Centimeter():
    with open("c_t_f_and_inches_to_cm_viceVersaa.txt",'a')as f:
        inches=eval(input("Enter the number in Inches : "))
        centimeter=inches * 2.54
        f.write("==Coversion of Inches to centimeter==\n")
        f.write(f"The number in centimeter is: {centimeter}\n")
        f.write("====================================\n\n")

def Centimeter_to_Inches():
    with open("c_t_f_and_inches_to_cm_viceVersaa.txt",'a')as f:
        f.write("==Coversion of Centimeter to Inches==\n")
        centimeter=eval(input("Enter the number in centimeter : "))
        inches=centimeter * 0.393701
        f.write(f"The number in centimeter is: {inches}\n")
        f.write("====================================\n\n")

print("----------------------------------")
print("<===Welcome to Unit Converter===>")
print("----------------------------------")
print("Press 1. Celsius to Fahrenheit ...")
print("Press 2. Fahrenheit to Celsius ...")
print("Press 3. Inches to Centimeter  ...")
print("Press 4. Centimeter to Inches  ...")
print("----------------------------------")
choice=int(input("Enter the Conversion : "))

if (choice==1):
    Celsius_to_Fahrenheit()
elif(choice==2):
    Fahrenheit_to_Celsius()
elif(choice==3):
    Inches_to_Centimeter()
elif(choice==4):
    Centimeter_to_Inches()