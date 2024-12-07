from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return None
    
if __name__ == "__main__":
    choice = input("What type of perosn do you want to create?(Student/Teacher)\n")
    person = PersonFactory.build_person(choice)

    if person:  
        person.person_method()    
    else:
        print("could not create person")    