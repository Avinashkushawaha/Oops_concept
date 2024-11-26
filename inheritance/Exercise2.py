class Battery:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def change(self):
        print(f"{self.name} battery is charging...")

    def discharge(self):
        print("{self.name} battery is discharging...")        


class Smartphone:
    def __init__(self, name,battery_name, battery_capacity):
        self.name = name
        self.battery = Battery(battery_name, battery_capacity)

    def launch_app(self, app_name):
        print(f"{self.name}launching {app_name}")

    def play_music(self, song_name):
        print(f"{self.name} playing {song_name}")     


apple = Smartphone("iphone 16","Li-ion",500)          
apple.play_music("dhoom machale")

print(apple.battery.name)
print(apple.battery.capacity)
apple.battery.change
