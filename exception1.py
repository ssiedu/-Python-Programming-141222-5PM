try:
    x=10
    y=int(input("Enter value : "))
    z=x/y
    print("value is : ",z)

except TypeError as e:
    print("Type mismatch")
    print(e)

except ZeroDivisionError:
    print("Zero Division Error")

except ValueError:
    print("Some Error occured")
