class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        return "Car is moving"

class Bike(Vehicle):
    def move(self):
        return "Bike is moving"

vehicles = [Car(), Bike()]
for vehicle in vehicles:
    print(vehicle.move())