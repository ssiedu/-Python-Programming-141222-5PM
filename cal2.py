num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number : "))
print(" Add\n Sub\n Mul\n Div\n")
ch=input(" Enter Your Choice : ")
match ch:
    case "Add":
        print("Addition :",num1+num2)
    case "Sub":
        print("Subtraction : ", num1-num2)
    case "Mul":
        print("Multiplication : ",num1*num2)
    case "Div":
        print("Division : ", num1/num2)
    case _:
        print("Please Enter Valid choice")

