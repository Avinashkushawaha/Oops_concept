from time import sleep
class Battery:
    type = 'Li-lion'
    def __init__(self,Capacity):
        self.capacity = Capacity
        
    def change(self, time):
        print(f'changing for {time} second,')
        sleep(time)


class Smartphone:
    def __init__(self, battery_capacity):
        self.battery = Battery(battery_capacity)

    def launch_app(self, name):
        print(f"launching {name}")
    def play_music (self, song):
        print(f"playing {song}")    


vivo = Smartphone(500)




print(vivo.battery.type)
print(vivo.battery.capacity)     
  

vivo.launch_app("Instagram")
vivo.play_music("Shape of You")
vivo.battery.change(2)
