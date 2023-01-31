class Student:
    def __init__(self):
        self.roll_no=121
        self.Name="Geeta"
    def __init__(self,rno=0,name="",per=0.0):
        self.roll_no=rno
        self.Name=name
        self.Per=per
    def display(self):
        print("Student Roll no : ", self.roll_no)
        print("Student Name    : ", self.Name)
        print("Student Percentage : ", self.Per)


'''r=int(input("Enter Roll no : "))
n=input("Enter Name : ")
p=eval(input("Enter Percentage : "))
s=Student(r,n,p)
s.display()'''

s1=Student(rno=111,per=78,name="shyam")
s1.display()

s2=Student()
s2.display()
