import unittest
import math
from main import Calculator


class TestCalculator(unittest.TestCase):

    def test_add_to_expression(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        # Test if the current expression matches the combination of the inputted numbers
        self.assertEqual(c.current_expression, '123')

    def test_append_operator(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        # Append an operator to the expression
        c.append_operator('+')
        # Test if the operator was appended to the total expression
        self.assertEqual(c.total_expression, '123+')
        # Test if the current expression is cleared
        self.assertEqual(c.current_expression, '')

    def test_evaluate_add(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('+')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '20')

    def test_evaluate_subtract(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('-')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '0')
    
    def test_evaluate_Multiply(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('*')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '100')

    def test_evaluate_Divide(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('/')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '1.0')
    
    def test_evaluate_add_and_subtract(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('+')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('-')
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(0)
        # Test if the calculator evaluates the expression correctly
        c.evaluate()
        self.assertEqual(c.current_expression, '-10')

    def test_square_a_number(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Square the inputted number
        c.square()
        # Test if the calculator gives the correct result
        self.assertEqual(c.current_expression, '100')


if __name__ == "__main__":
    unittest.main()
