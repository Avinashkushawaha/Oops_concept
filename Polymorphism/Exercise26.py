class Shape:
    def draw(self):
        raise  NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Square(Shape):
    def draw(self):
        return "Drawing a square"

shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())
        
