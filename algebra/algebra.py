import sympy as sp


def solve_algebraic_expression(expression):
    x = sp.symbols('x')
    equation = sp.Eq(sp.sympify(expression.split(
        '=')[0]), sp.sympify(expression.split('=')[1]))
    solutions = sp.solve(equation, x)

    # Convert solutions to decimal format
    decimal_solutions = [float(sol.evalf()) for sol in solutions]

    return decimal_solutions


def main():
    print("Simple Algebraic Expression Solver Bot")
    while True:
        expression = input(
            "Please input algebraic expression (e.g., 3*x + 2 = 5): ")

        if expression.lower() == 'exit':
            print("Exiting the bot. Goodbye!")
            break

        try:
            solutions = solve_algebraic_expression(expression)
            print("Solutions are:", solutions)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
