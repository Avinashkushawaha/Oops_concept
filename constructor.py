class Student:
    numberOfStudents = 0
    schoolName = "MAPS"

    def __init__(self, name,rollNumber,marks):
        #print(id(self))
        self.rollNumber = rollNumber
        self.name = name
        self.__marks = marks
        self.numberOfStudents = Student.numberOfStudents + 1
        Student.numberOfStudents = Student.numberOfStudents + 1

    def getMarks(self):
        return self.__marks

    def study(self):
        print("I am "+ str(self.rollNumber)+"and I am studying")

    def play(self):
        print("pdh liya, now going to play")


s1 = Student("Mayank",1,90) 
s2 = Student("Goku",2,50) 

# print(s1.getMarks())
# s1.getMarks = 45
print(s1.mark)          