class Base:
    def getdata(self):
        print("Hello Everyone! This is a Base class")


class derive(Base):
    def print(self):
        print("Hello! This is derive class")


d=derive()
d.getdata()
d.print()
