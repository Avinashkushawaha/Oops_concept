class Animal:
    def sound(self):
        print("Animal sound")

class Lion(Animal):
    def sound(self):
        print("Roar")

class Elephant(Animal):
    def sound(self):
        print("Trumpet")

zoo = [Lion(), Elephant()]
for animal in zoo:
    animal.sound()                        