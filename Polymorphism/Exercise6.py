class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"
    
def make_sound(animal):
    print(animal.sound())


make_sound(Dog())        
make_sound(Cat())