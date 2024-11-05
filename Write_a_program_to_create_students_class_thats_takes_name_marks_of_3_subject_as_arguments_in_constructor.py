#create student class that takes names & marks of 3 subject as arguments in constructor
class student:
    def __init__(self, name, marks,):
        self.name = name
        self.marks = marks


    def get_avg(self):
        sum = 0
        for val in  self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)        


s1 = student("tony stark", [99, 98, 97])       
s1.get_avg()