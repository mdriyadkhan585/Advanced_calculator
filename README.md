# Advanced Python Calculator

![Logo](logo.svg)

---
## Overview

This Python calculator script is a powerful tool that supports a wide range of mathematical operations. It includes basic arithmetic calculations, advanced mathematical functions, matrix operations, polynomial calculations, integration, differentiation, statistical analysis, and function plotting. This README provides a detailed guide on the usage, features, and code structure of the calculator.

## Features

1. **Basic Arithmetic Operations**
   - Addition
   - Subtraction
   - Multiplication
   - Division
   - Exponentiation

2. **Advanced Mathematical Functions**
   - Square Root
   - Factorial
   - Trigonometric Functions (sin, cos, tan, asin, acos, atan)

3. **Matrix Operations**
   - Addition
   - Subtraction
   - Multiplication
   - Determinant Calculation
   - Matrix Inversion
   - Eigenvalues Calculation

4. **Polynomial Operations**
   - Evaluation of Polynomials
   - Finding Roots of Polynomials

5. **Integration and Differentiation**
   - Definite Integration of Functions
   - Differentiation of Functions

6. **Statistical Analysis**
   - Mean
   - Median
   - Variance
   - Standard Deviation

7. **Function Plotting**
   - Visualize Functions Using Matplotlib

## Prerequisites

To run this script, you need Python and several Python libraries installed:

- `numpy`
- `scipy`
- `matplotlib`

Install these libraries using pip:

```bash
pip install numpy scipy matplotlib
```
```bash
git clone https://github.com/mdriyadkhan585/Advanced_calculator
cd Advanced_calculator
```

## How to Use

1. **Run the Script**: Execute the script in your Python environment.

   ```bash
   python simple-calculator.py
   python level-calculator.py
   python next-level-calculator.py
   python advanced-calculator.py
   python pro-calculator.py
   ```

2. **Select an Operation**: Choose from the operations listed in the menu.

3. **Provide Inputs**: Follow the prompts to enter the required values.

4. **View Results**: The results will be displayed based on the operation chosen.

## Program Description

### Basic Arithmetic Operations

- **Addition**: `add(x, y)` - Returns the sum of `x` and `y`.
- **Subtraction**: `subtract(x, y)` - Returns the difference between `x` and `y`.
- **Multiplication**: `multiply(x, y)` - Returns the product of `x` and `y`.
- **Division**: `divide(x, y)` - Returns the quotient of `x` divided by `y`, handling division by zero.
- **Exponentiation**: `exponent(x, y)` - Returns `x` raised to the power of `y`.

### Advanced Mathematical Functions

- **Square Root**: `square_root(x)` - Computes the square root of `x`, with error handling for negative inputs.
- **Factorial**: `factorial(x)` - Computes the factorial of `x`, with validation for non-integer and negative inputs.
- **Trigonometric Functions**: 
  - `trig_sin(x)` - Returns the sine of angle `x` (in degrees).
  - `trig_cos(x)` - Returns the cosine of angle `x` (in degrees).
  - `trig_tan(x)` - Returns the tangent of angle `x` (in degrees).
  - `trig_asin(x)` - Returns the arc sine of `x` (domain: [-1, 1]).
  - `trig_acos(x)` - Returns the arc cosine of `x` (domain: [-1, 1]).
  - `trig_atan(x)` - Returns the arc tangent of `x`.

### Matrix Operations

- **Addition**: `matrix_operations()` - Adds two 2x2 matrices.
- **Subtraction**: `matrix_operations()` - Subtracts one 2x2 matrix from another.
- **Multiplication**: `matrix_operations()` - Multiplies two 2x2 matrices.
- **Determinant Calculation**: `matrix_operations()` - Computes the determinant of a 2x2 matrix.
- **Matrix Inversion**: `matrix_operations()` - Computes the inverse of a 2x2 matrix, with error handling for singular matrices.
- **Eigenvalues Calculation**: `matrix_operations()` - Finds the eigenvalues of a 2x2 matrix.

### Polynomial Operations

- **Evaluation**: `polynomial_operations()` - Evaluates a polynomial at a given value of `x`.
- **Finding Roots**: `polynomial_operations()` - Finds the roots of a polynomial using its coefficients.

### Integration and Differentiation

- **Integration**: `function_integration()` - Computes the definite integral of a user-defined function over a specified interval.
- **Differentiation**: `function_differentiation()` - Computes the derivative of a user-defined function.

### Statistical Analysis

- **Mean**: `statistical_operations()` - Calculates the mean of a dataset.
- **Median**: `statistical_operations()` - Calculates the median of a dataset.
- **Variance**: `statistical_operations()` - Calculates the variance of a dataset.
- **Standard Deviation**: `statistical_operations()` - Calculates the standard deviation of a dataset.

### Function Plotting

- **Plotting**: `plot_function()` - Plots a user-defined mathematical function over a specified range.

## Code Structure

1. **Function Definitions**: Contains functions for all the operations mentioned.
2. **Menu System**: Provides an interactive menu for users to select operations.
3. **Input Handling**: Prompts the user for inputs and processes them accordingly.
4. **Error Handling**: Includes error handling for invalid inputs and mathematical errors.
5. **Plotting**: Uses `matplotlib` to generate plots for visual representation of functions.

## Example

1. **Run the script** using `python calculator.py`.
2. **Choose an Operation**: For example, select `1` for addition.
3. **Enter Numbers**: Provide two numbers when prompted.
4. **View Results**: The result of the addition will be displayed.

## Contribution

Contributions are welcome! If you have suggestions for new features or improvements, please open an issue or submit a pull request.

## Acknowledgements

- **NumPy**: For numerical computations.
- **SciPy**: For scientific and technical computing.
- **Matplotlib**: For plotting and visualization.


### Instructions:

- **Installation**: Ensure that `numpy`, `scipy`, and `matplotlib` are installed in your Python environment.
- **Running the Script**: Save the Python code in a file named `calculator.py` and execute it.
- **Using the Calculator**: Follow the interactive prompts to perform various mathematical operations.
