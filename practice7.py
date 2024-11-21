class Employee:
    Company = "Google"
    Location = "Benguluru"
    Ceo = "Sunder Pichai"

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        print("Employee object created...")

    def emp_info(self):
        print(f"Employee of : {Employee.Company}")  
        print(f"Employee name : {self.name}")  
        print(f"Employee id : {self.emp_id}")
        print(f"Employee salary : {self.salary}")


john = Employee("John cona", 420, 5000)        
john.emp_info()
