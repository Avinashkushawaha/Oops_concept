class cat:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} runing in stealth mode... ")    

    def sound(self):
        print(f"{self.name}meows...")

class Tiger(cat):
    def __init__(self, name):
        super().__init__(name) 

    def hunt(self):
        print(f"{self.name} is hunting...")

    def sound(self):
        print(f"{self.name}roars | rowwrr...")   


kitty = cat("kitty")
kitty.sound()
richard_parker = Tiger("Richard Parker")
richard_parker.sound()           
