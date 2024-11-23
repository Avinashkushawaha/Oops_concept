class BasicMath:
    @staticmethod
    def add(num1:float, num2:int|float):
        return num1 + num2
    
    @staticmethod
    def Subtract(num1:int|float, num2:int|float):
        return num1 - num2
    
    @staticmethod
    def multiply(num1:int|float, num2:int|float):
        return num1 * num2
    
    @staticmethod
    def divide(num1:int|float, num2:int|float):
        return num1 / num2
    
b1 = BasicMath()
print(b1. add(10, 20))    
print(b1. Subtract(10, 20))    
print(b1. multiply(10, 20))    
print(b1. divide(10, 20))   