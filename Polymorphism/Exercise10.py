class Calulator:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num

        return result   
    
calc = Calulator()
print("Multiplying 2 numbers: ", calc.multiply(4, 5)) 
print("multiplying 3 numbers : ", calc.multiply(2, 3, 4))   