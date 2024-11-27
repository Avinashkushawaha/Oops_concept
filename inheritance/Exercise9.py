class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Animal))  
print(issubclass(Dog, Animal))  
