def make_sound(animal):
    return animal.sound()

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(make_sound(animal))