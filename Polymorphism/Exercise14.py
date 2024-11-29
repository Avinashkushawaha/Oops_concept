class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age if age else "Unknown"  

    def display(self):  
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("John")
p2 = Person("Jane", 25)


p1.display()
p2.display()
