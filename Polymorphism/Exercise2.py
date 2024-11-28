class integer :
    def __init__(self, value:int):
        self.value = value
    def __add__(self, address):
        return self.value + address .value
    def __sub__(self,address):
        return self.value - address.value
    

num1 = integer(10)
num2 = integer(20)


print(num1 + num2)
print(num1 - num2)
1