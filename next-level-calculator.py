import math
import cmath

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def factorial(x):
    if x < 0 or not x.is_integer():
        return "Error! Factorial of negative or non-integer number."
    return math.factorial(int(x))

def trig_sin(x):
    return math.sin(math.radians(x))

def trig_cos(x):
    return math.cos(math.radians(x))

def trig_tan(x):
    return math.tan(math.radians(x))

def complex_operations():
    print("Complex number operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    
    real1 = float(input("Enter the real part of the first complex number: "))
    imag1 = float(input("Enter the imaginary part of the first complex number: "))
    real2 = float(input("Enter the real part of the second complex number: "))
    imag2 = float(input("Enter the imaginary part of the second complex number: "))
    
    c1 = complex(real1, imag1)
    c2 = complex(real2, imag2)
    
    if choice == '1':
        result = c1 + c2
    elif choice == '2':
        result = c1 - c2
    elif choice == '3':
        result = c1 * c2
    elif choice == '4':
        if c2 == 0:
            return "Error! Division by zero."
        result = c1 / c2
    else:
        return "Invalid choice"
    
    return result

def main():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Trigonometric Functions (sin, cos, tan)")
        print("9. Complex Number Operations")
        print("10. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")
        
        if choice == '10':
            print("Exiting...")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if choice == '8':
                angle = float(input("Enter the angle in degrees: "))
                print(f"sin({angle}) = {trig_sin(angle)}")
                print(f"cos({angle}) = {trig_cos(angle)}")
                print(f"tan({angle}) = {trig_tan(angle)}")
            elif choice == '9':
                print(complex_operations())
            else:
                if choice == '6':
                    num = float(input("Enter number: "))
                    print(f"Square root of {num} = {square_root(num)}")
                elif choice == '7':
                    num = float(input("Enter number: "))
                    print(f"Factorial of {num} = {factorial(num)}")
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(f"{num1} + {num2} = {add(num1, num2)}")
                    elif choice == '2':
                        print(f"{num1} - {num2} = {subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"{num1} * {num2} = {multiply(num1, num2)}")
                    elif choice == '4':
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    elif choice == '5':
                        print(f"{num1} ** {num2} = {exponent(num1, num2)}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
  
