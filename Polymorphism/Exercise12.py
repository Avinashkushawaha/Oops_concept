class shape:
    def draw(self):
        print("Drawing a shape")

class circle(shape):
    def draw(self):
        print("Drawing a circle")

shape = circle()        
shape.draw()
