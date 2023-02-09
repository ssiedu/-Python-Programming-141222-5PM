import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rno=rno;
        self.name=name;
        self.s1,self.s2=0.0,0.0;
    def getdata(self):
        print("Enter Marks of student : ")
        self.s1=eval(input("Enter Marks of subject1 : "))
        self.s2=eval(input("Enter Marks of subject2 : "))
    def display(self):
        print("Roll No : ", self.rno)
        print("Name    : ", self.name)
        print("subject1 : ", self.s1)
        print("subject2 : ", self.s2)

S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.getdata()
S2.getdata()
fout=open("Record","wb")
pickle.dump(S1,fout)
pickle.dump(S2,fout)
fout.close()

S=Student()
fin=open("Record","rb")
try:
    while True:
        S=pickle.load(fin)
        S.display()
except:
    fin.close()
    
