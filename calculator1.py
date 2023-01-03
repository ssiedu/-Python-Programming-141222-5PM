num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number : "))
print(" 1.Add\n 2.Sub\n 3.Mul\n 4.Div\n")
ch=int(input(" Enter Your Choice : "))
match ch:
    case 1:
        print("Addition :",num1+num2)
    case 2:
        print("Subtraction : ", num1-num2)
    case 3:
        print("Multiplication : ",num1*num2)
    case 4:
        print("Division : ", num1/num2)
    case _:
        print("Please Enter Valid choice")
