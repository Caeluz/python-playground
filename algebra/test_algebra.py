import unittest
from algebra import solve_algebraic_expression


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

if __name__ == "__main__":
    unittest.main()