class Person:
   def __init__(self, name, occ):
       self.name = name
       self.occ = occ

   def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Avi", "Developer")
b = Person("Divya", "Hr")

a.info()
b.info()



