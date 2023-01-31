class Employee:
    def __init__(self):
        self.id=int(input("Enter Employee Id : "))
        self.name=input("Enter Employee Name : ")
        self.sal=eval(input("Enter Employee salary : "))
    def display(self):
        print("Employee Id : ",self.id)
        print("Employee Name : ",self.name)
        print("Employee Salary : ",self.sal)


emp=Employee()
emp.display()

emp1=Employee()
emp1.display()
