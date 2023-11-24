import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


def solve_algebraic_expression(expression):
    x = sp.symbols('x')
    equation = sp.Eq(sp.sympify(expression.split(
        '=')[0]), sp.sympify(expression.split('=')[1]))
    solutions = sp.solve(equation, x)

    # Convert solutions to decimal format
    decimal_solutions = [float(sol.evalf()) for sol in solutions]

    return decimal_solutions

def validate_expression(expression):
    try:
        transformations = (standard_transformations +
                           (implicit_multiplication_application,))
        parse_expr(expression, transformations=transformations)
        return True
    except Exception as e:
        print("Invalid expression. Please enter a valid algebraic expression.")
        return False


def main():
    print("Simple Algebraic Expression Solver Bot")
    while True:
        expression = input(
            "Please input algebraic expression (e.g., 3*x + 2 = 5): ")

        if expression.lower() == 'exit':
            print("Exiting the bot. Goodbye!")
            break

        if not validate_expression(expression):
            continue

        try:
            solutions = solve_algebraic_expression(expression)
            print("Solutions are:", solutions)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
