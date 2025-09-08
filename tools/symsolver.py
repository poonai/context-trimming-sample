import sympy as sp

def quadratic_equation_solver(equation_str):
    """
    Solves a quadratic equation and returns its roots.
    
    Parameters:
    equation_str (str): A string representing a quadratic equation in the form 
                        "ax^2 + bx + c = 0" or similar formats.
    
    Returns:
    tuple: A tuple containing the roots of the quadratic equation.
    """
    # Define the symbol
    x = sp.Symbol('x')
    
    # Clean up the equation string
    equation_str = equation_str.replace("^", "**").strip()
    
    # Check if the equation contains an equals sign
    if "=" in equation_str:
        left_side, right_side = equation_str.split("=")
        # Move everything to the left side
        equation_str = f"({left_side}) - ({right_side})"
    
    # Parse the equation string into a sympy expression
    expr = sp.sympify(equation_str)
    
    # Solve the equation
    solutions = sp.solve(expr, x)
    
    return solutions

def quadratic_derivative(equation_str):
    """
    Finds the derivative of a quadratic equation.
    
    Parameters:
    equation_str (str): A string representing a quadratic equation in the form 
                        "ax^2 + bx + c = 0" or similar formats.
    
    Returns:
    sympy.Expr: The derivative of the quadratic expression.
    """
    # Define the symbol
    x = sp.Symbol('x')
    
    # Clean up the equation string
    equation_str = equation_str.replace("^", "**").strip()
    
    # Check if the equation contains an equals sign
    if "=" in equation_str:
        left_side, right_side = equation_str.split("=")
        # Move everything to the left side
        equation_str = f"({left_side}) - ({right_side})"
    
    # Parse the equation string into a sympy expression
    expr = sp.sympify(equation_str)
    
    # Find the derivative
    derivative = sp.diff(expr, x)
    
    return derivative

def evaluate_equation(equation_str, x_value):
    """
    Evaluates an equation at a given input value.
    
    Parameters:
    equation_str (str): A string representing an equation.
    x_value (float): The value to substitute for the variable x.
    
    Returns:
    float: The result of evaluating the equation at the given input.
    """
    # Define the symbol
    x = sp.Symbol('x')
    
    # Clean up the equation string
    equation_str = equation_str.replace("^", "**").strip()
    
    # Check if the equation contains an equals sign
    if "=" in equation_str:
        left_side, right_side = equation_str.split("=")
        # Move everything to the left side
        equation_str = f"({left_side}) - ({right_side})"
    
    # Parse the equation string into a sympy expression
    expr = sp.sympify(equation_str)
    
    # Substitute the value and evaluate
    result = expr.subs(x, x_value)
    
    return float(result)

# # Example usage:
# if __name__ == "__main__":
#     # Example equations
#     equations = [
#         "x^2 - 5*x + 6 = 0",
#         "2*x^2 + 4*x - 6 = 0",
#         "x^2 = 4"
#     ]
    
#     for eq in equations:
#         print(f"Equation: {eq}")
#         roots = quadratic_equation_solver(eq)
#         print(f"Roots: {roots}")
        
#         # Test the derivative function
#         derivative = quadratic_derivative(eq)
#         print(f"Derivative: {derivative}")
        
#         # Test the evaluate function with x = 2
#         value = evaluate_equation(eq, 2)
#         print(f"Value at x = 2: {value}")
#         print()
