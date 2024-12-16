from abc import ABC, abstractmethod
class Polygon (ABC):
    @abstractmethod
    def roofsides (self):
        pass
class Triangle (Polygon):
    # overriding abstract method
    def roofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    def roofsides(self):
        print("I have 5 sides")
class Hexagon (Polygon):
    def roofsides(self):
        print("I have 6 sides")                



triangle = Triangle()
triangle.roofsides()  

pentagon = Pentagon()
pentagon.roofsides()  

hexagon = Hexagon()
hexagon.roofsides() 
