num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number : "))
print(" 1.+\n 2.-\n 3.*\n 4./\n")
ch=input(" Enter Your Choice : ")
match ch:
    case '+':
        print("Addition :",num1+num2)
    case '-':
        print("Subtraction : ", num1-num2)
    case '*':
        print("Multiplication : ",num1*num2)
    case '/':
        print("Division : ", num1/num2)
    case _:
        print("Please Enter Valid choice")

