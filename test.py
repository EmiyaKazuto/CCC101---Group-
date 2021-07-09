import unittest
import math
from main import Calculator


class TestCalculator(unittest.TestCase):

## for basic functions

    def test_add_to_expression(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        self.assertEqual(c.current_expression, '123')

    def test_append_operator(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        c.append_operator('+')
        self.assertEqual(c.total_expression, '123+')
        self.assertEqual(c.current_expression, '')

    def test_append_operator2(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        c.append_operator('-')
        self.assertEqual(c.total_expression, '123-')
        self.assertEqual(c.current_expression, '')

    def test_append_operator3(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        c.append_operator('x')
        self.assertEqual(c.total_expression, '123x')
        self.assertEqual(c.current_expression, '')

    def test_append_operator4(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        c.append_operator('/')
        self.assertEqual(c.total_expression, '123/')
        self.assertEqual(c.current_expression, '')

    def test_evaluate_add(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '20')

    def test_evaluate_subtract(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '0')
    
    def test_evaluate_Multiply(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('*')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '100')

    def test_evaluate_Divide(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '1.0')
    
    def test_evaluate_add_and_subtract(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '-10')

    def test_evaluate_multiply_and_divide(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('*')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '200.0')

    def test_evaluate_multiply_and_add(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('*')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '1005')

    def test_evaluate_multiply_and_minus(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('*')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '995')

    def test_evaluate_divide_and_minus(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '5.0')

    def test_evaluate_divide_and_add(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '15.0')

    def test_all_operations(self):
        c= Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(5)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(2)
        c.append_operator('+')
        self.assertEqual(c.total_expression, '10+100-50/2+')

    def test_all_operations_evaluate(self):
        c= Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.append_operator('-')
        c.add_to_expression(5)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression(2)
        c.append_operator('*')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '-15.0')


## for pi function

    def test_add_pi(self):
        c = Calculator()
        c.add_to_expression('π')
        self.assertEqual(c.current_expression, 'π')
    
    def test_add_pi_evaluate(self):
        c = Calculator()
        c.add_to_expression('π')
        c.evaluate()
        self.assertEqual(c.current_expression, '3.14159265358')

    def test_piAndNumber_add(self):
        c = Calculator()
        c.add_to_expression('π')
        c.add_to_expression('+')
        c.add_to_expression('5')
        self.assertEqual(c.current_expression, 'π+5')

    def test_piAndNumber_add_evaluate(self):
        c = Calculator()
        c.add_to_expression('π')
        c.add_to_expression('+')
        c.add_to_expression('5')
        c.evaluate()
        self.assertEqual(c.current_expression, '8.14159265358')
    
    def test_piAndNumber_subtract(self):
        c = Calculator()
        c.add_to_expression('π')
        c.add_to_expression('-')
        c.add_to_expression('1')
        self.assertEqual(c.current_expression, 'π-1')

    def test_piAndNumber_subtract_evaluate(self):
        c = Calculator()
        c.add_to_expression('π')
        c.add_to_expression('-')
        c.add_to_expression('1')
        c.evaluate()
        self.assertEqual(c.current_expression, '2.14159265358')

    def test_piAndNumber_multiply(self):
        c = Calculator()
        c.add_to_expression('π')
        c.add_to_expression('*')
        c.add_to_expression('1')
        self.assertEqual(c.current_expression, 'π*1')
    
    def test_piAndNumber_multiply_evaluate(self):
        c = Calculator()
        c.add_to_expression('π')
        c.append_operator('*')
        c.add_to_expression('1')
        c.evaluate()
        self.assertEqual(c.current_expression, '3.14159265358')
    
    def test_pi5(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('*π')
        c.evaluate()
        self.assertEqual(c.current_expression, '15.7079632679')


## for ln function

    def test_ln_function(self):
        c = Calculator()
        c.add_to_expression('ln(')
        c.add_to_expression('5')
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '1.60943791243')

    def test_ln_add(self):
        c = Calculator()
        c.add_to_expression('ln(')
        c.add_to_expression('5')
        c.evaluate()
        self.assertEqual(c.current_expression,  'Error')

    def test_lnError(self):
        c = Calculator()
        c.add_to_expression('ln(')
        c.add_to_expression('5')
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_ln2(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*ln(')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '3.21887582486')


## for log function

    def test_log(self):
        c = Calculator()
        c.add_to_expression('log(')
        c.add_to_expression(10)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '1.0')

    def test_logError(self):
        c = Calculator()
        c.add_to_expression('log(')
        c.add_to_expression('10')
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')

    def test_log2(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*log(')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '2.0')


## for absolute function

    def test_absolute(self):
        c = Calculator()
        c.add_to_expression('abs(')
        c.add_to_expression('-')
        c.add_to_expression(8)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '8.0')

    def test_absolute2(self):
        c = Calculator()
        c.add_to_expression('abs(')
        c.add_to_expression('-')
        c.add_to_expression(8)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_absolute3(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('*abs(')
        c.add_to_expression('-')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '25.0')


## for e 

    def test_efunction1(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*')
        c.add_to_expression('e(')
        c.add_to_expression(2)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '14.7781121978')

    def test_efunction2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.append_operator('+')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '7.71828182845')

    def test_efunction_error(self):
        c = Calculator()
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_efunction3(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('*e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '13.5914091422')


## for sin function

    def test_sin_function(self):
        c = Calculator()
        c.add_to_expression('sin(')
        c.add_to_expression(9)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '0.89399666360')
    
    def test_sin_error(self):
        c = Calculator()
        c.add_to_expression('sin(')
        c.add_to_expression(9)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_sin2(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*sin(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '0.0')
     
   
## for cos function

    def test_cos_function(self):
        c = Calculator()
        c.add_to_expression('cos(')
        c.add_to_expression(9)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '-0.4480736161')
    
    def test_cos_error(self):
        c = Calculator()
        c.add_to_expression('tan(')
        c.add_to_expression(9)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_cos_function1(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*cos(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '2.0')


## for tan function

    def test_tan_function(self):
        c = Calculator()
        c.add_to_expression('tan(')
        c.add_to_expression(9)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '-1.9952004122')
    
    def test_tan_function2(self):
        c = Calculator()
        c.add_to_expression('tan(')
        c.add_to_expression(1)
        c.add_to_expression(8)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    
    def test_tan_function3(self):
        c = Calculator()
        c.add_to_expression(2)
        c.add_to_expression('*tan(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '0.0')


## for parentheses

    def test_parentheses(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('*(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '5')
    
    def test_parenthesis2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('*(')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.append_operator('+')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '75')


## for squared

    def test_square_a_number(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression('²')
        c.evaluate()
        self.assertEqual(c.current_expression, '100')
    
    def test_square_a_number2(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(5)
        c.add_to_expression('²')
        c.evaluate()
        self.assertEqual(c.current_expression, '11025')

    def test_square_a_number3(self):
        c = Calculator()
        c.add_to_expression(3)
        c.add_to_expression('²')
        c.evaluate()
        self.assertEqual(c.current_expression, '9')
    

## for square root

    def test_squareroot_a_number(self):
        c = Calculator()
        c.add_to_expression('sqrt(')
        c.add_to_expression(2)
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '5.0')
    
    def test_squareroot_a_number2(self):
        c = Calculator()
        c.add_to_expression('sqrt(')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '10.0')

    def test_squareroot_a_number_error(self):
        c = Calculator()
        c.add_to_expression('sqrt(')
        c.add_to_expression(2)
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')


## for cubed

    def test_cube_a_number(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression('³')
        c.evaluate()
        self.assertEqual(c.current_expression, '1000')

    def test_cube_a_number2(self):
        c = Calculator()
        c.add_to_expression(3)
        c.add_to_expression('³')
        c.evaluate()
        self.assertEqual(c.current_expression, '27')

    def test_cube_a_number(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(5)
        c.add_to_expression('³')
        c.evaluate()
        self.assertEqual(c.current_expression, '3375')


## for permutation

    def test_permutation(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('P')
        c.add_to_expression(3)
        c.evaluate()
        self.assertEqual(c.current_expression, '60')
    
    def test_permutation2(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(5)
        c.add_to_expression('P')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '360360')

    def test_permutation3(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(1)
        c.add_to_expression('P')
        c.add_to_expression(1)
        c.add_to_expression(3)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')

    def test_permmutation4(self):
        c = Calculator()
        c.add_to_expression(-2)
        c.add_to_expression('P')
        c.add_to_expression(-1)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')


## for combination

    def test_combination(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('C')
        c.add_to_expression(3)
        c.evaluate()
        self.assertEqual(c.current_expression, '10')

    def test_combination2(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression('C')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        self.assertEqual(c.current_expression, '66')

    def test_combination_error(self):
        c = Calculator()
        c.add_to_expression(-2)
        c.add_to_expression('C')
        c.add_to_expression(-1)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')

    def test_combination_error2(self):
        c = Calculator()
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression('C')
        c.add_to_expression(1)
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, 'Error')
    

## for exponent

    def test_exponent(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('E')
        c.add_to_expression(2)
        c.evaluate()
        self.assertEqual(c.current_expression, '500')
    
    def test_exponent2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('E')
        c.add_to_expression(-3)
        c.evaluate()
        self.assertEqual(c.current_expression, '0.005')
    
    def test_exponent3(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(3)
        c.add_to_expression('E')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '5300000')    


## for delete

    def test_delete_function(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.delete()
        self.assertEqual(c.current_expression, '567')

    def test_delete_function2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.add_to_expression('+')
        c.delete()
        self.assertEqual(c.current_expression, '5678')

    def test_delete_function3(self):
        c = Calculator()
        c.add_to_expression('(')
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.add_to_expression('+')
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.delete()
        self.assertEqual(c.current_expression, '(56+78)')

    def test_delete_function4(self):
        c = Calculator()
        c.add_to_expression('ln(')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression('E')
        c.delete()
        self.assertEqual(c.current_expression, 'ln(e(1')


## for delete all

    def test_delete_all(self):
        c = Calculator()
        c.add_to_expression(5)
        c.append_operator('+')
        c.add_to_expression(6)
        c.append_operator('-')
        c.add_to_expression(2)
        c.clear()
        self.assertEqual(c.current_expression, '')
    
    def test_delete_all2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.append_operator('+')
        c.add_to_expression(6)
        c.append_operator('-')
        c.add_to_expression(2)
        c.evaluate()
        c.clear()
        self.assertEqual(c.current_expression, '')

    def test_delete_all3(self):
        c = Calculator()
        c.add_to_expression('tan(')
        c.add_to_expression(0)
        c.clear()
        self.assertEqual(c.current_expression, '')


## for ans

    def test_answer_function(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.append_operator('+')
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.evaluate()
        c.clear()
        c.answer()
        self.assertEqual(c.current_expression, 'Ans')

    def test_answer_function2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.append_operator('+')
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.evaluate()
        c.clear()
        c.add_to_expression('Ans')
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(3)
        self.assertEqual(c.current_expression, 'Ans+13')

    def test_answer_function2(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression(6)
        c.append_operator('+')
        c.add_to_expression(7)
        c.add_to_expression(8)
        c.evaluate()
        c.clear()
        c.add_to_expression('Ans')
        c.append_operator('+')
        c.add_to_expression(1)
        c.add_to_expression(3)
        c.evaluate()
        self.assertEqual(c.current_expression, '147')
    

## for complicated expressions, mas komplikado pa sa inyong relasyon.

    def test_compl1(self):
        c = Calculator()
        c. add_to_expression(1)
        c.append_operator('+')
        c.add_to_expression(2)
        c.append_operator('-')
        c.add_to_expression(3)
        c.append_operator('*')
        c.add_to_expression(4)
        c.append_operator('/')
        c.add_to_expression(5)
        c.evaluate()
        self.assertEqual(c.current_expression, '0.60000000000')

    def test_compli2(self):
        c = Calculator()
        c. add_to_expression(5)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression('(')
        c.add_to_expression('ln(')
        c.add_to_expression('e(1')
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression(25)
        c.append_operator('-')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '2.5')
        
    def test_compli3(self):
        c = Calculator()
        c. add_to_expression(5)
        c.add_to_expression(0)
        c.append_operator('/')
        c.add_to_expression('(')
        c.add_to_expression('(')
        c.add_to_expression('ln(')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('+')
        c.add_to_expression('tan(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression(25)
        c.append_operator('-')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '2.5')

    def test_compli4(self):
        c = Calculator()
        c.add_to_expression('(')
        c.add_to_expression('log(')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression('ln(')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('/')
        c.add_to_expression('(')
        c.add_to_expression(5)
        c.append_operator('+')
        c.add_to_expression('sin(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression(1)
        c.append_operator('-')
        c.add_to_expression(3)
        c.add_to_expression(')')
        c.evaluate()
        self.assertEqual(c.current_expression, '0.5')

    def test_compli5(self):
        c = Calculator()
        c.add_to_expression(5)
        c.add_to_expression('P')
        c.add_to_expression(3)
        c.append_operator('+')
        c.add_to_expression(2)
        c.add_to_expression('C')
        c.add_to_expression(1)
        c.append_operator('*')
        c.add_to_expression(5)
        c.add_to_expression('C')
        c.add_to_expression(2)
        c.append_operator('/')
        c.add_to_expression(3)
        c.add_to_expression('P')
        c.add_to_expression(1)
        c.append_operator('-')
        c.add_to_expression(6)
        c.add_to_expression('P')
        c.add_to_expression(3)
        c.evaluate()
        self.assertEqual(c.current_expression, '-59.0')

    def test_compli6(self):
        c = Calculator()
        c.add_to_expression('π')
        c.append_operator('+')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.append_operator('-')
        c.add_to_expression('log(')
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression('log(')
        c.add_to_expression(5)
        c.add_to_expression(')')
        c.append_operator('/')
        c.add_to_expression('ln(')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('+')
        c.add_to_expression('sin(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('+')
        c.add_to_expression('cos(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('+')
        c.add_to_expression('tan(')
        c.add_to_expression(0)
        c.add_to_expression(')')
        c.append_operator('*')
        c.add_to_expression(5)
        c.add_to_expression('P')
        c.add_to_expression(1)
        c.append_operator('-')
        c.add_to_expression(5)
        c.add_to_expression('C')
        c.add_to_expression(2)
        c.append_operator('+')
        c.add_to_expression(5)
        c.append_operator('/')
        c.add_to_expression(1)
        c.evaluate()
        self.assertEqual(c.current_expression, '1.16090447771')

    def compli7(self):
        c = Calculator()
        c.add_to_expression('(')
        c.add_to_expression(5)
        c.add_to_expression('²')
        c.append_operator('/')
        c.add_to_expression(5)
        c.add_to_expression('³')
        c.add_to_expression(')')
        c.append_operator('+')
        c.add_to_expression('sqrt(')
        c.add_to_expression(36)
        c.add_to_expression(')')
        c.append_operator('-')
        c.add_to_expression(10)
        c.add_to_expression('C')
        c.add_to_expression(9)
        c.append_operator('/')
        c.add_to_expression('(')
        c.add_to_expression('cos(')
        c.add_to_expression('e(')
        c.add_to_expression(1)
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.add_to_expression(')')
        c.append_operator('-')
        c.add_to_expression(1)
        c.evaluate()
        self.assertEqual(c.current_expression, '16.1681123382')



if __name__ == "__main__":
    unittest.main()
