class Addition:
    def input(self,fnum,snum):
        self.num1=fnum
        self.num2=snum
    def add(self):
        self.add=self.num1+self.num2
    def display(self):
        print("Addition is : ",self.add)


a=Addition()
x=int(input("Enter First Number : "))
y=int(input("Enter Second Number : "))
a.input(x,y)
a.add()
a.display()
