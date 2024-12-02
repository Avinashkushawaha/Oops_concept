class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a quick!")

def make_it_quack(something):
    something.quack()                

duck = Duck()    
person = Person()
make_it_quack(duck)
make_it_quack(person)