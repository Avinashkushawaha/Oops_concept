class AutoMobile:
    def __init__(self, name):
        self.name = name


    def accelerate(self, amount):
        print(f"accelerating {self.name} by {amount}%") 

    def apply_brake(self, amount):
        print(f"Appying brake on {self.name}, reducing speed by {amount}%")   


class Scooter(AutoMobile):
    minor = 2
    Seat = 2
    def __init__(self,name):
        super().__init__(name)

    def turn_right(self):
        print(f"{self.name} turning right")      

    def turn_left(self):
        print(f"{self.name} turning left")    


class Bike(Scooter):
    gears = 5
    def __init__(self,name):
        super().__init__(name)

    def shift_gear(self,gear_number):
        print(f"Shifting to gear {gear_number} ")           


himalyan = Bike("Himalyan")
himalyan.accelerate(50) 
himalyan.turn_left()
himalyan.turn_right()
himalyan.shift_gear(3)       

 