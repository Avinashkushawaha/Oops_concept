class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"my name is {self.name}")     

    @staticmethod
    def eat(dish):
        print(f"i am eating {dish}")




person1 = person("Alice")

person1.introduce()  
person1.eat("pizza")  
