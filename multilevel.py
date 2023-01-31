class First:
    def getdata(self):
        self.l=eval(input("Enter length of rectangle : "))
        self.b=eval(input("Enter breadth of rectangle : "))


class Second(First):
    def calculate(self):
        self.area=self.l*self.b


class Third(Second):
    def display(self):
        print("Area of rectangle : ", self.area)



T=Third()
T.getdata()
T.calculate()
T.display()
