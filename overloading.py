class Area:
    def findArea(self,a=None,b=None):
        if(a!=None and b!=None):
            print("Area of rectangle : ", a*b)
        elif(a!=None and b==None):
            print("Square : ", a*a)
        else:
            print("Nothoing")



a=Area()
a.findArea()
a.findArea(2)
a.findArea(2,3)
