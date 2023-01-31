class Employee:
    def getdata(self):
        self.name=input("Enter Employee name : ")
        self.age =int(input("Enter Employee age : "))


class Employee1(Employee):
    def getinfo(self):
        self.id=int(input("Enter Employee Id : "))
        self.sal=eval(input("Enter Employee salary : "))


class Info(Employee1):
    def display(self):
        print("Employee Name : ", self.name)
        print("Employee Age  : ", self.age)
        print("Employee id   : ", self.id)
        print("Employee sal  : ", self.sal)


I=Info()
I.getdata()
I.getinfo()
I.display()
