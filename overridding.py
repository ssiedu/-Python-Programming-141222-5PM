class Base:
    def Hello(self):
        print("This is Base class Function")

class Derive(Base):    
    def Hello(self):
        super().Hello()
        print("This is derive class function")



D=Derive()
D.Hello()
#D.Hello()
