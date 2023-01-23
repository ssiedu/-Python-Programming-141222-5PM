def product(fnum,snum,tnum):
    print("First Number : ",fnum)
    print("Second Number : ",snum)
    print("Third Number : ",tnum)
    #r=fnum*snum*tnum
    return fnum*snum*tnum
    #print("product of three numbers : ",result)




x=eval(input("Enter First Number : "))
y=eval(input("Enter Second Number : "))
z=eval(input("Enter Third Number : "))
#res=product(y,x,z)
print("product of numbers : ",product(x,y,z))
