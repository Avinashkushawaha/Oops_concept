class Brain():
    def __init__(self,owner):
        self.owner = owner

    def think_good(self):
        print(f"{self.owner} is used to think good")

    def think_evil(self):
        print(f"{self.owner} is thinking evil..")


class Human:
    brain = Brain("shadab")
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def walk(self):
        print(f"{self.name} is walking...")

    def sleep(self):
        print(f"{self.name} is sleeping...")


class planet:
    human = Human("shadab", 99) 
    def __init__(self, name):           
         self.name = name 

    def rotate(self):
        print(f"{self.name} is rotating...")

    def revolve(self):  
        print(f"{self.name} is revolve...")


planet = planet("mother father")     
planet.revolve()  
planet.rotate()        
planet.human.brain.think_evil()
planet.human.brain.think_good()
planet.human.walk()
planet.human.sleep()


