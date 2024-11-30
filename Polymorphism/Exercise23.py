class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

class Multiplier:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value * x
    
adder = Adder(5)
multiplier = Multiplier(3)

print(adder(10))
print(multiplier(10))
                