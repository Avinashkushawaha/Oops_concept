from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car moves on four wheels")   

class Bike(Vehicle):
    def move(self):
        print("Bike moves on two wheels ")

car = Car()
bike = Bike()

car.move()
bike.move()

