class polygon (ABC):
    @abstractmethod
    def roofsides (self):
        pass
class Triangles (polygon):
    # overriding abstract method
    def roofsides(self):
        print("I have 3 sides")
class pentagon(polygon):
    def roofsides(self):
        print("I have 5 sides"):
class hexagon (polygon):
    def roofsides(self):
        print("I have 6 sides")                