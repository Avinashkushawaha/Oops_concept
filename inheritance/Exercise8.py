class Animal:
    def speak(self):
        print("Animal makes a sound")

class Flyable:
    def fly(self):
        print("Can fly")

class Bird(Animal, Flyable):  
    pass


bird = Bird()
bird.speak()  
bird.fly()    
