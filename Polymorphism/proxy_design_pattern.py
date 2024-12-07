from abc import ABCMeta, abstractclassmethod

class Iperson(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        """ Interface Methode """

class Person(Iperson):
    def person_method(self):
        print("I am a person!")

class Proxy                