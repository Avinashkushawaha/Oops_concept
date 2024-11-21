class BasicMath:
    pI = 3.14
    tau = 6.28
    golden_ratio = 1.618
    Eulen_constant = 2.718

    def add(self, num1: float, num2: float) ->float: 
         return num1 + num2
    
    def subtract(self, num1: float, num2: float) ->float:
         return num1 - num2
    
    def multiply(self, num1: float, num2: float) ->float:
         return num1 * num2
    
    def divide(self, num1: float, num2: float) ->float:
         if num2 != 0:   
          return num1 / num2
         else:
            return "Cannot divide by zero"
         
    


math_obj = BasicMath()
print(math_obj.add(5, 3))
print(math_obj.subtract(5, 3))
print(math_obj.multiply(5, 3))
print(math_obj.divide(5, 0))



      