class Math:
    def add(self, a, b, c=0):
        return a + b + c
    
obj = Math()
print(obj.add(2, 3))
print(obj.add(2, 3, 4))
