from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    @abstractmethod
    def calculate_eta(self, distance):
        pass

    @abstractmethod
    def load(self, weight, dimensions=None):
        pass

    def get_vehicle_type(self):
        return self.vehicle_type


class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck")

    def calculate_eta(self, distance, is_heavy_load=False):
        speed = 60  
        if is_heavy_load:
            speed *= 0.8 
        return distance / speed

    def load(self, weight, dimensions=None):
        if dimensions:
            volume = dimensions[0] * dimensions[1] * dimensions[2]
            if volume > 100: 
                return "Exceeds volume capacity!"
        return f"Loaded {weight}kg."


class Bike(Vehicle):
    def __init__(self):
        super().__init__("Bike")

    def calculate_eta(self, distance, bad_weather=False):
        speed = 25  
        if bad_weather:
            speed *= 0.7  
        return distance / speed

    def load(self, weight, dimensions=None):
        if weight > 10:  
            return "Exceeds weight capacity!"
        return f"Loaded {weight}kg."


class Drone(Vehicle):
    def __init__(self):
        super().__init__("Drone")

    def calculate_eta(self, distance):
        speed = 80  
        if distance > 10:  
            raise ValueError("Out of range!")
        return distance / speed

    def load(self, weight, dimensions=None):
        if weight > 5: 
            return "Exceeds weight capacity!"
        return f"Loaded {weight}kg."


def simulate_transportation():
    vehicles = [Truck(), Bike(), Drone()]
    distance = 15 

    for vehicle in vehicles:
        print(f"Vehicle Type: {vehicle.get_vehicle_type()}")
        
       
        try:
            if isinstance(vehicle, Truck):
                eta = vehicle.calculate_eta(distance, is_heavy_load=True)
            elif isinstance(vehicle, Bike):
                eta = vehicle.calculate_eta(distance, bad_weather=True)
            elif isinstance(vehicle, Drone):
                eta = vehicle.calculate_eta(distance)
            print(f"Estimated Time of Arrival: {eta:.2f} hours")
        except ValueError as e:
            print(f"Error: {e}")

    
        if isinstance(vehicle, Truck):
            print(vehicle.load(50, (2, 2, 2))) 
        elif isinstance(vehicle, Bike):
            print(vehicle.load(8)) 
        elif isinstance(vehicle, Drone):
            print(vehicle.load(4))  

        print("-" * 30)


simulate_transportation()
