import math
import numpy as np
from numpy.polynomial import Polynomial

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

def trig_asin(x):
    if x < -1 or x > 1:
        return "Error! Domain for asin is [-1, 1]."
    return math.degrees(math.asin(x))

def trig_acos(x):
    if x < -1 or x > 1:
        return "Error! Domain for acos is [-1, 1]."
    return math.degrees(math.acos(x))

def trig_atan(x):
    return math.degrees(math.atan(x))

def matrix_operations():
    print("Matrix operations (2x2 matrices):")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Determinant")
    choice = input("Enter choice (1/2/3/4): ")
    
    def get_matrix_input():
        print("Enter the elements of the matrix row-wise:")
        a = float(input("a11: "))
        b = float(input("a12: "))
        c = float(input("a21: "))
        d = float(input("a22: "))
        return np.array([[a, b], [c, d]])

    matrix1 = get_matrix_input()
    matrix2 = get_matrix_input()

    if choice == '1':
        result = matrix1 + matrix2
    elif choice == '2':
        result = matrix1 - matrix2
    elif choice == '3':
        result = np.dot(matrix1, matrix2)
    elif choice == '4':
        result = [np.linalg.det(matrix1), np.linalg.det(matrix2)]
    else:
        return "Invalid choice"
    
    return result

def polynomial_operations():
    print("Polynomial operations:")
    print("1. Evaluate polynomial")
    print("2. Find roots of polynomial")
    choice = input("Enter choice (1/2): ")
    
    degree = int(input("Enter the degree of the polynomial: "))
    coefficients = [float(input(f"Enter coefficient for x^{i}: ")) for i in range(degree + 1)]
    
    poly = Polynomial(coefficients)
    
    if choice == '1':
        x = float(input("Enter the value of x: "))
        result = poly(x)
    elif choice == '2':
        result = poly.roots()
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
        print("8. Trigonometric Functions (sin, cos, tan, asin, acos, atan)")
        print("9. Matrix Operations")
        print("10. Polynomial Operations")
        print("11. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")
        
        if choice == '11':
            print("Exiting...")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if choice == '8':
                angle = float(input("Enter the angle in degrees: "))
                print(f"sin({angle}) = {trig_sin(angle)}")
                print(f"cos({angle}) = {trig_cos(angle)}")
                print(f"tan({angle}) = {trig_tan(angle)}")
                print(f"asin({trig_sin(angle)}) = {trig_asin(trig_sin(angle))}")
                print(f"acos({trig_cos(angle)}) = {trig_acos(trig_cos(angle))}")
                print(f"atan({trig_tan(angle)}) = {trig_atan(trig_tan(angle))}")
            elif choice == '9':
                print(matrix_operations())
            elif choice == '10':
                print(polynomial_operations())
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
