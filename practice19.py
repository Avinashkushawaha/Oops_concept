class Plane:
    propellers = True
    wings = 2
    def __init__(self, name):
        self.name = name

    def take_off(self):
        print(f"{self.name} is taking off fasten your seat bealt")

    def land(self):
        print(f"{self.name} is landing...")


class CargoPlane(Plane):
    volume = "30m^3"

    def __init__(self, name):
        super().__init__(name)

    def load_item(self, item):
        print(f"loading{item} into {self.name}")

    def unload_item(self, item):
        print(f"unloading {item} from {self.name}")


class FighterJet(Plane):
    def __init__(self, name):
        super().__init__(name)

    def launch_missile(self, target):
        print(f"{self.name} is launching missile on {target}...")

    def fire_at_target(self, target):
        print(f"{self.name} firing at {target}...")


mig21 = FighterJet("Mig21")       
mig21.take_off()
mig21.launch_missile("Kiran")
mig21.land()


