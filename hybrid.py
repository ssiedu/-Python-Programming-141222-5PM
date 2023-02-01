class Base1:
    def getdata(self):
        self.l=int(input("Enter length of rectangle : "))
        self.b=int(input("Enter breadth of rectangle : "))


class child1(Base1):
    def calculate(self):
        self.area=self.l*self.b


class child2:
    def getradius(self):
        self.r=int(input("Enter radius of circle : "))
    def calculate1(self):
        self.area1=3.14*self.r*self.r


class subchild(child1,child2):
    def display(self):
        print("Area of rectangle : ", self.area)
        print("Area of circle    : ", self.area1)



s=subchild()
s.getdata()
s.calculate()
s.getradius()
s.calculate1()
s.display()









        
