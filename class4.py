class Area:
    def getdata(self):
        self.l=eval(input("Enter length of rectangle : "))
        self.b=eval(input("Enter breadth of rectangle : "))
    def calculate(self):
        self.a=self.l * self.b
    def display(self):
        print("Area of rectangle :%.2f"%self.a)


obj=Area()
obj.getdata()
obj.calculate()
obj.display()

print("lenght of rectangle : ", self.l)
print("breadth of rectangle : ", self.b)
