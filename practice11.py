class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Point Constructor")

class Joint(Point):
    def __init__(self):
        print("Joint Constructor")
        super(). __init__(10, 20)


J1 = Joint()    
print(J1.__dict__)    
        
    
