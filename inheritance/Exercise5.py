from math import pi
class circle:
    ''' class dedicated to calculated area and perimeter of any circle with the given radius'''
    perimeter = '2 * pi * radius'
    area = "pi * (radius ** 2)"

    def __init__(self, radius :int |float):
        self.radius = radius


    def perimeter(self):
        """used to calculate the perimeter of a circle with the given radius"""
        return 2 * pi * self.radius 

    def get_area(self):
        """used to calculate the area of a circle with the given radius """         
        return pi * (self.radius ** 2)
    
    @classmethod
    def from_diameter(cls, diameter:int|float):
        """class method that return an object of circle through diatmeter"""
        radius = diameter / 2
        return cls (radius)
    

c1 = circle(10)
c1 = circle.from_diameter(20)
c2 = c1.from_diameter(20)

print(f"Circle with radius {c2.radius} has perimeter: {c2.perimeter()}")
print(f"Circle with radius {c2.radius} has area: {c2.get_area()}")

c3 = c2.from_diameter(40)
print(f"Circle with radius {c3.radius} has perimeter: {c3.perimeter}")
print(f"circle with radius {c3.radius} has area:{c3.get_area()}")