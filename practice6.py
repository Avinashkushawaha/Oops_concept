class Car :
    wheels = 4
    steering_wheels = True
    horn = True

    def __init__(self, power, torque, mileage, car_type  ):
        self.power = power
        self.torque = torque
        self.mileage = mileage
        self.car_type = car_type

fortuner = Car ('280hp' , '300nm', '7kmpl', 'suv')

print({'power':fortuner.power, 'torque':fortuner.torque,'mileage':fortuner.mileage, 'type': fortuner.car_type})
