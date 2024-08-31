import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.linalg import inv, eig
from numpy.polynomial import Polynomial
from sympy import symbols, diff, sympify

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
    return np.sqrt(x)

def factorial(x):
    if x < 0 or not x.is_integer():
        return "Error! Factorial of negative or non-integer number."
    return np.math.factorial(int(x))

def trig_sin(x):
    return np.sin(np.radians(x))

def trig_cos(x):
    return np.cos(np.radians(x))

def trig_tan(x):
    return np.tan(np.radians(x))

def trig_asin(x):
    if x < -1 or x > 1:
        return "Error! Domain for asin is [-1, 1]."
    return np.degrees(np.arcsin(x))

def trig_acos(x):
    if x < -1 or x > 1:
        return "Error! Domain for acos is [-1, 1]."
    return np.degrees(np.arccos(x))

def trig_atan(x):
    return np.degrees(np.arctan(x))

def matrix_operations():
    print("Matrix operations (2x2 matrices):")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Determinant")
    print("5. Inverse")
    print("6. Eigenvalues")
    choice = input("Enter choice (1/2/3/4/5/6): ")

    def get_matrix_input():
        print("Enter the elements of the matrix row-wise:")
        a = float(input("a11: "))
        b = float(input("a12: "))
        c = float(input("a21: "))
        d = float(input("a22: "))
        return np.array([[a, b], [c, d]])

    matrix1 = get_matrix_input()

    if choice in ['1', '2', '3']:
        matrix2 = get_matrix_input()

    if choice == '1':
        result = matrix1 + matrix2
    elif choice == '2':
        result = matrix1 - matrix2
    elif choice == '3':
        result = np.dot(matrix1, matrix2)
    elif choice == '4':
        result = np.linalg.det(matrix1)
    elif choice == '5':
        try:
            result = inv(matrix1)
        except np.linalg.LinAlgError:
            result = "Error! Matrix is singular and cannot be inverted."
    elif choice == '6':
        result = eig(matrix1)[0]
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

def function_integration():
    print("Integration:")
    def func(x):
        return eval(func_str)
    
    func_str = input("Enter the function to integrate (e.g., 'x**2 + 2*x + 1'): ")
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))
    
    result, error = quad(func, a, b)
    return f"Integral result: {result}, with error estimate: {error}"

def function_differentiation():
    print("Differentiation:")
    def func(x):
        return eval(func_str)
    
    x = symbols('x')
    func_str = input("Enter the function to differentiate (e.g., 'x**2 + 2*x + 1'): ")
    func_expr = sympify(func_str)
    
    derivative = diff(func_expr, x)
    return f"Derivative: {derivative}"

def statistical_operations():
    print("Statistical operations:")
    data = list(map(float, input("Enter data values separated by spaces: ").split()))
    
    return {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Variance": np.var(data),
        "Standard Deviation": np.std(data)
    }

def plot_function():
    import matplotlib.pyplot as plt
    
    func_str = input("Enter the function to plot (e.g., 'x**2 + 2*x + 1'): ")
    x = np.linspace(-10, 10, 400)
    y = [eval(func_str.replace('x', str(val))) for val in x]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=func_str)
    plt.title('Function Plot')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

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
        print("11. Integration")
        print("12. Differentiation")
        print("13. Statistical Operations")
        print("14. Plot Function")
        print("15. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
        
        if choice == '15':
            print("Exiting...")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']:
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
            elif choice == '11':
                print(function_integration())
            elif choice == '12':
                print(function_differentiation())
            elif choice == '13':
                print(statistical_operations())
            elif choice == '14':
                plot_function()
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
    
