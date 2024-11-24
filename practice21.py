class MotherBoard:
    components = ["resister", "capacitor", "inductor", "diode", "transistor"]
    base = "Si"
    def usage(self):
        print(f"some electronic process")

class AudioDevice(MotherBoard):
    def volume_down(self, amount):
        print(f"decreasing volume by{amount}%")

class VideoDevice(MotherBoard):
    def decreas_brightness(self, amount):
        print(f"decreasing brightness by {amount} %")

class Television(AudioDevice, VideoDevice):
    def turn_on(self):
        print(f"Turning the Tv on...")        
    def turn_off(self):
        print(f"Turning the Tv off...")

class SmartPhone(Television):
    def launch_app(self, name):
        print(f"launching {name}...")        
    def make_call(self, Contact):
        print(f"Contacting {Contact}...")  


smartPhone = SmartPhone()
smartPhone.turn_on()
smartPhone.turn_off()
smartPhone.launch_app("Youtube")
smartPhone.make_call("john")
smartPhone.volume_down(20)
smartPhone.decreas_brightness(30)
smartPhone.usage()



