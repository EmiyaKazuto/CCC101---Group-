from math import *

def trig_sine(arg):
    return sin(arg)

def trig_cosine(arg):
    return cos(arg)

def trig_tangent(self):
    return tan(arg)

def trig_secant(arg):
    return sec(arg)

def trig_cosecant(arg):
    return csc(arg)

def trig_cotangent(arg):
    return cot(arg)

def permutation(n,r):
    factorial = math.factorial
    if n >= r >= 0:
        return factorial(n) // factorial(n-r)

def combination(n,r):
    factorial = math.factorial
    if 0 <= r <= n:
        return factorial(n) // factorial(r) // factorial(n-r)


class Calculator:
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def append_calculator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def evaluate_expression(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""

        except Exception as e:
            self.current_expression = "Math Error"

    def square_a_number(self):
        self.current_expression = (str(eval(f"{self.current_expression}**2")))

    def cube_a_number(self):
        self.current_expression = (str(eval(f"{self.current_expression}**3")))

    def sqrt_of_a_number(self):
        if self.current_expression > 0:
            self.current_expression = (str(eval(f"{self.current_expression}**0.5")))
        else: 
            self.current_expression = "Math Error"
    
    def cuberoot_of_a_number(self):
        self.current_expression = (str(eval(f"{self.current_expression}**(1/3)")))
    
    def delete_a_number(self):
        self.current_expression = self.current_expression[:-1]

    def clear_calculator(self):
        self.current_expression = ""
        self.total_expression = ""

