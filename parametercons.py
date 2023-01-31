class Student:
    def __init__(self,rno,name,per):
        self.roll_no=rno
        self.Name=name
        self.Per=per
    def display(self):
        print("Student Roll no : ", self.roll_no)
        print("Student Name    : ", self.Name)
        print("Student Percentage : ", self.Per)


r=int(input("Enter Roll no : "))
n=input("Enter Name : ")
p=eval(input("Enter Percentage : "))
s=Student(r,n,p)
s.display()
