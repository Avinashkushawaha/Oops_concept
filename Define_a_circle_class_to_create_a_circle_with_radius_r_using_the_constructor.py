#define a circle class to create a circle with radius r using the constructor

class Cirlce:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius ** 2
        
        
    def perimeter(self):
        return 2 * 22/7 * self.radius

c1 = Cirlce(21)
print(c1.area())
print(c1.perimeter())
