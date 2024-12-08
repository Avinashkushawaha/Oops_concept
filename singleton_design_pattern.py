from abc import ABCMeta, abstractmethod

class Iperson(metaclass=ABCMeta):

    @abstractmethod
    def get_data():
        """ implement in child class """