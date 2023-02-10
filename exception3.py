try:
    x=int(input("Enter number in between 1-100: "))
    if x>100 or x<1:
        raise ArithmeticError

except ArithmeticError:
    print("value out of range")

else:
    print("value in range ")
