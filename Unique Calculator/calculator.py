import math

class UniqueCalculator:
    def __init__(self):
        print("==> Welcome to the Unique Calculator!")
        print("=====================================")

    def basic_operations(self):
        print("Basic Operations:")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /, %, **, //): ")

        if operation == '+':
            print(f"Result: {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1 * num2}")
        elif operation == '/':
            print(f"Result: {num1 / num2}")
        elif operation == '%':
            print(f"Result: {num1 % num2}")
        elif operation == '**':
            print(f"Result: {num1 ** num2}")
        elif operation == '//':
            print(f"Result: {num1 // num2}")
        else:
            print("Invalid operation!")

    def unit_conversion(self):
        print("Unit Conversion:")
        unit = input("Choose conversion type (km-miles, c-f, kg-lbs): ")
        value = float(input("Enter the value to convert: "))

        if unit == 'km-miles':
            print(f"{value} km is equal to {value * 0.621371} miles")
        elif unit == 'c-f':
            print(f"{value}°C is equal to {(value * 9/5) + 32}°F")
        elif unit == 'kg-lbs':
            print(f"{value} kg is equal to {value * 2.20462} lbs")
        else:
            print("Invalid conversion type!")

    def scientific_operations(self):
        print("Scientific Operations:")
        operation = input("Choose the operation (sqrt, sin, cos, tan, log): ")
        value = float(input("Enter the value: "))

        if operation == 'sqrt':
            print(f"Result: {math.sqrt(value)}")
        elif operation == 'sin':
            print(f"Result: {math.sin(math.radians(value))}")
        elif operation == 'cos':
            print(f"Result: {math.cos(math.radians(value))}")
        elif operation == 'tan':
            print(f"Result: {math.tan(math.radians(value))}")
        elif operation == 'log':
            print(f"Result: {math.log(value)}")
        else:
            print("Invalid operation!")

    def run(self):
        while True:
            print("\nMain Menu:")
            print("1. Basic Operations")
            print("2. Unit Conversion")
            print("3.  Scientific Operations")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.basic_operations()
            elif choice == '2':
                self.unit_conversion()
            elif choice == '3':
                self.scientific_operations()
            elif choice == '4':
                print("Exiting... Thank you for using the Unique Calculator!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    calculator = UniqueCalculator()
    calculator.run()
