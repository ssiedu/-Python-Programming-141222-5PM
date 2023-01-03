num= int(input("Enter any number : "))
if num%5==0 and num%7==0:
    print("Number is divisible by both")
elif num%5==0:
    print("Number is divisible by 5")
elif num%7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by both")
