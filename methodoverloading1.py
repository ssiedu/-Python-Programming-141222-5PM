from multipledispatch import dispatch

@dispatch(int,int)
def product(first,second):
    result=first*second
    print("Product of two integer value : ",result)

@dispatch(int,int,int)
def product(first,second,third):
    result=first*second*third
    print("product of three integer value : ",result)


@dispatch(int,float)
def product(first,second):
    result=first*second
    print("product of two different value : ",result)

@dispatch(int,float,float)
def product(first,second,third):
    result=first*second*third
    print("product of three different value : ",result)



product(10,20,30)
product(2,1.1,2.3)
product(10,20)
product(10,2.2)


    
