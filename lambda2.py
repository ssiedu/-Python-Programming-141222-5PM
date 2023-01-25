var=lambda num1,num2 : num1 if(num1>num2) else num2


num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
res=var(num1,num2)
print("largest Number is : ",res)
