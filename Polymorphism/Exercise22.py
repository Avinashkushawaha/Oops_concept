from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on the road"

vehicles = [Car(), Bicycle()]
for vehicle in vehicles:
    print(vehicle.move())
