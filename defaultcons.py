class Exchange:
    def getdata(self):
        self.num1=int(input("Enter First Number : "))
        self.num2=int(input("Enter Second Number : "))
    def swap(self):
        self.num1,self.num2=self.num2,self.num1
    def display(self):
        print("First Number : ",self.num1)
        print("Second Number : ",self.num2)


Ex=Exchange()
Ex.getdata()
Ex.swap()
Ex.display()
