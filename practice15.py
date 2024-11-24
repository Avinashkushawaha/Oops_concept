class Mammal:
    finger = 5

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping ....DND")    


class Monkey(Mammal):
    tail = True
    eyes = 2
    def fight(self):
        print("I am fighting ...")

    def drink(self):
        print("I am drinking....")

class Homosapiens(Monkey):
    tail = False
    hands = 2

    def think(self):
        print("I can think ...")            


you = Homosapiens()        
you.think()
you.sleep()
you.drink()
