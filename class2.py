class Addition:
    def input(self):
        self.num1=int(input("Enter First number : "))
        self.num2=int(input("Enter Second Number : "))
    def add(self):
        self.add=self.num1+self.num2
    def display(self):
        print("Addition is : ",self.add)


a=Addition()
a.input()
a.add()
a.display()
