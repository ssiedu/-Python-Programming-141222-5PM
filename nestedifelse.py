num=int(input("Enter any number : "))
if num==0:
    print("Zero")
elif num>0:
    print("Positive Number ")
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("negative Number")
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
