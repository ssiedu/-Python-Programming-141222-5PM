class Student:
    def getdata(self):
        self.name=input("Enter Name of student : ")
        self.roll_no=int(input("Enter roll no of student : "))
        self.per =eval(input("Enter percentage of student: "))
    def display(self):
        print("Name of student : ", self.name)
        print("rollno of student : ",self.roll_no)
        print("Percentage of student : ",self.per)


s1=Student()
s1.getdata()
s2=Student()
s2.getdata()
s1.display()
s2.display()
