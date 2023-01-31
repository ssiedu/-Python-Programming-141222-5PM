class simple_Interest:
    def __init__(self):
        self.p=eval(input("Enter Amount : "))
        self.r=eval(input("Enter rate of interest : "))
        self.t=eval(input("Enter time in year : "))
    def calculate(self):
        self.si=(self.p*self.r*self.t)/100
        self.total = self.p+self.si
    def display(self):
        print("Simple Interest : ",self.si)
        print("Total Amount    : ",self.total)

SI=simple_Interest()
SI.calculate()
SI.display()
