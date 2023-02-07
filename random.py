import random

while True:
    ch=input('''
Game Start.....
1.Yes(y/Y)
2.No|Exit(n/'N')
''')
    if ch=='y' or ch=='Y':
        cinput=random.randrange(1,6)
        uinput=int(input("Enter any number: "))
        if cinput>uinput:
            print("Computer Number : ",cinput)
            print("Your guessing number is too low")

        elif cinput<uinput:
            print("Computer Number : ",cinput)
            print("Your guessing number is too high")

        else:
            print("Computer Number : ",cinput)
            print("Your guessing number is equal to computer number ")

    else:
       break;


    


    
