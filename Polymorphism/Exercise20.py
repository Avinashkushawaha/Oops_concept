from abc import ABC, abstractmethod
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyable, Swimmable):
    def fly(self):
        print("Duck is flying")

    def swim(self):
        print("Duck is swimming")    

duck = Duck()
duck.fly()  
duck.swim()       