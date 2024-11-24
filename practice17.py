class Bird:
    wings = True

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying ...")

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking...")    

    def run(self):
        print(f"{self.name} is running...")    

class Dragon(Animal, Bird):
    def __init__(self, name):
        super().__init__(name)

    def breathe_fire(self, dracarys):
        print(f"{self.name} breathing fire {dracarys}")



drogon = Dragon("Drogon")  

drogon.fly()
drogon.walk()
drogon.breathe_fire("dracarys")

                    