class Calculator:
    def sum(self, * args):
        return sum(args)
    
calc = Calculator()    
print(calc.sum(1, 2, 3))
print(calc.sum(1, 2, 3, 4))
