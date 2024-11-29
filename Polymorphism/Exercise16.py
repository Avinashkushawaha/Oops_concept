class Calculater:
    def add(self, a, b):
        if isinstance(a, float) or isinstance(b, float):
            return float(a + b)
        return a + b
    
calc = Calculater()
print(calc.add(5, 3))
print(calc.add(5.5, 3))
