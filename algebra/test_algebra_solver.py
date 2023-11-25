import unittest
from algebra_solver import solve_algebraic_expression


class TestAlgebraSolver(unittest.TestCase):
    def test_single_solution(self):
        expression = "2*x + 3 = 7"
        expected_solution = [2.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_multiple_solutions(self):
        expression = "x**2 - 4 = 0"
        expected_solutions = [-2.0, 2.0]
        actual_solutions = solve_algebraic_expression(expression)
        self.assertEqual(actual_solutions, expected_solutions)

    def test_no_solution(self):
        expression = "x + 5 = x + 10"
        expected_solutions = []
        actual_solutions = solve_algebraic_expression(expression)
        self.assertEqual(actual_solutions, expected_solutions)

    def test_invalid_expression(self):
        expression = "2x + 3 = 7"
        with self.assertRaises(Exception):
            solve_algebraic_expression(expression)

    def test_integer_solution(self):
        expression = "3*x - 6 = 0"
        expected_solution = [2.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_decimal_solution(self):
        expression = "0.5*x + 1 = 2"
        expected_solution = [2.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_exponential_solution(self):
        expression = "2**x = 8"
        expected_solution = [3.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_negative_solution(self):
        expression = "-x + 5 = 2"
        expected_solution = [3.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_zero_solution(self):
        expression = "0*x + 2 = 5"
        expected_solution = []
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

    def test_large_solution(self):
        expression = "100*x - 1000 = 0"
        expected_solution = [10.0]
        actual_solution = solve_algebraic_expression(expression)
        self.assertEqual(actual_solution, expected_solution)

if __name__ == "__main__":
    unittest.main()