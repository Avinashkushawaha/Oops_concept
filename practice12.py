class SoftAnimal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating ...")

    def sleep(self):
        print(f"{self.name} is sleeping ...")        

    def drink(self):
        print(f"{self.name} is drinking ...")     

class KungFuPanda(SoftAnimal):
    def __init__(self, name):
        self.name = name

    def fight(self):
        print(f"{self.name} knows Kung Fu")

    def climb_tree(self):
        print(f"{self.name} can climb a tree")

    def eat(self):
        print(f"{self.name} is bhukkad ...")        

print(dir (KungFuPanda))
po = KungFuPanda("po")
po.sleep()
po.eat()
po.climb_tree()
po.fight()
po.drink()
po.eat()



