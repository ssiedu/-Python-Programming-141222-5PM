class First:
    def getFirst(self):
        self.p=int(input("Enter principle amount : "))


class Second:
    def getSecond(self):
        self.r=int(input("Enter rate of interest : "))


class Third:
    def getThird(self):
        self.t=int(input("Enter time in year : "))


class child(First,Second,Third):
    def calculate(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.si+self.p
    def display(self):
        print("Simple Interest : ",self.si)
        print("Total Amount    : ",self.total)

c=child()
c.getFirst()
c.getSecond()
c.getThird()
c.calculate()
c.display()







        
