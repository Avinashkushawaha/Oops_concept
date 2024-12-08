from abc import ABCMeta, abstractmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ implement in child class """

    @abstractmethod
    def print_department():
        """ implement in child class """

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees   

    def print_department(self):
        print(f"Accounting Deparment: {self.employees}")

class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees 