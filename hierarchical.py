class Base:
    def getdata(self):
        self.num1=eval(input("Enter First Number : "))
        self.num2=eval(input("Enter Second Number : "))


class Add(Base):
    def getAddition(self):
        self.add=self.num1+self.num2
        print("Addition is : ",self.add)


class Sub(Base):
    def getSub(self):
        self.sub=self.num1-self.num2
        print("Subtraction is : ", self.sub)

class Mul(Base):
    def getMul(self):
        self.mul=self.num1*self.num2
        print("Multiplication is : ",self.mul)



a=Add()
a.getdata()
a.getAddition()
s=Sub()
s.getdata()
s.getSub()
m=Mul()
m.getdata()
m.getMul()




        
