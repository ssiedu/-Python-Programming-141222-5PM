class First:
    def __init__(self):
        self.num1=int(input("Enter First Number : "))
        self.num2=int(input("Enter Second Number : "))
        self.num3=int(input("Enter Third Number : "))


class Second(First):
    def calculate(self):
        self.product= self.num1*self.num2*self.num3
    def display(self):
        print("Product of three Number : ",self.product)


s=Second()
#s.getdata()
s.calculate()
s.display()
