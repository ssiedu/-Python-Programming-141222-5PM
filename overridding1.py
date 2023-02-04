class First:
    def getdata(self):
        self.x=int(input("Enter First Value : "))


class Second(First):
    def getdata(self):
        super().getdata()
        self.y=int(input("Enter Second Value : "))

class Third(Second):
    def getdata(self):
        super().getdata()
        self.z=int(input("Enter Third Value : "))
    def display(self):
        print("Sum is : ", self.x+self.y+self.z)


T=Third()
T.getdata()
T.display()
