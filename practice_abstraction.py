

from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ElectricCar(Car):
    def start_engine(self):
        print("Starting the electric engine...")

    def drive(self):
        print("Driving the electric car silently...")

class GasolineCar(Car):
    def start_engine(self):
        print("Starting the gasoline engine...")

    def drive(self):
        print("Driving the gasoline car with engine noise...")

def start_and_drive(car: Car):
    car.start_engine()
    car.drive()


electric_car = ElectricCar()
gasoline_car = GasolineCar()


start_and_drive(electric_car)
start_and_drive(gasoline_car)
