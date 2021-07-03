import math

sin, cos, tan = math.sin, math.cos, math.tan
sqrt = math.sqrt
power = math.pow
π = math.pi
abs = math.fabs
log = math.log10
ln = math.log
e = math.e

class Calculator():
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""
        self.prev_ans = ''

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def pi_function(self):
        ('π' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' )
                           else '*π' )
    
    def log_function(self):
        self.current_expression = 'log(' + self.current_expression

    def ln_function(self):
        self.current_expression = 'ln(' + self.current_expression

    def abs_function(self):
        self.current_expression = 'abs(' + self.current_expression
    
    def e_function(self):
        ('e' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' )
                           else '*e' )

    def trig_sine(self):
        self.current_expression =  'sin(' + self.current_expression

    def trig_cosine(self):
        self.current_expression =  'cos(' + self.current_expression

    def trig_tangent(self):
        self.current_expression =  'tan(' + self.current_expression

    def squared(self):
        self.current_expression = self. current_expression + '²'

    def sqrt(self):
        self.current_expression = 'sqrt(' + self.current_expression

    def cubed(self):
        self.current_expression = self. current_expression + '³'

    def perm(self):
        self.current_expression = self.current_expression + 'P'

    def comb(self):
        self.current_expression = self.current_expression + 'C'

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""

    def delete(self):
        self.current_expression = str(self.current_expression[:-1])

    def answer(self):
        self.current_expression = 'Ans' + self.current_expression


    def exp_function(self):
        self.current_expression = self.current_expression + 'E'

    def evaluate(self):
        self.total_expression += self.current_expression
        x = self.total_expression
        
        try:
            if '²' in x or '³' in x or 'E' in x or 'P' in x or 'C' in x or 'Ans' in x:
                x = x.replace('²', '**2').replace('³', '**3').replace('E','*10**').replace('Ans',f'{self.prev_ans}')
                pc = []
                operands = ['+', '-', '*', '/']
                for i in range(len(x)):
                    if x[i] == 'P' or x[i] == 'C':
                        term = ''
                        y = z = i
                        while y > -1 and x[y] not in operands:
                            term = x[y] + term
                            y -= 1
                        while (z+1) < len(x) and x[z+1] not in operands:
                            term += x[z+1]
                            z += 1
                        pc.append(term)
                for term in pc:
                    if 'P' in term:
                        n,r = term.split('P')
                        n,r = int(n), int(r)
                        if 0 <= r <= n: 
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({n}-{r})')
                    elif 'C' in term:
                        n,r = term.split('C')
                        n,r = int(n), int(r)
                        if 0 <= r <= n:
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({r})' + '//' + f'math.factorial({n}-{r})' )
            self.current_expression = str(eval(x))
            
        except Exception:
            self.current_expression = "Math Error"   
        
        self.prev_ans = self.current_expression[:]
        self.total_expression = ""
        self.current_expression = self.current_expression[:13]
        return self.current_expression
