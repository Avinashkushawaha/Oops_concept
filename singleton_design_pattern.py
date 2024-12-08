from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self):
        """ implement in child class """
        pass
class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton.__instance = PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("singleton cannot be instantiated more than once!")
        
              
        self.name = name
        self.age = age
      
    def get_data(self):
        return f"Name: {self.name}, Age: {self.age}"

    @staticmethod
    def print_data():
        if PersonSingleton.__instance is not None:  
            print(PersonSingleton.__instance.get_data())


p = PersonSingleton.get_instance()
p.print_data()

p2 = PersonSingleton.get_instance()
p2.print_data()

print(p is p2)


        
