count=int(input("How many students data u want to enter : "))
print("Enter Student Information : ")
fout=open("Student.txt","w")

for i in range(count):
    
    name=input("Enter name of student : ")
    rollno=int(input("Enter Student rollno : "))
    per=eval(input("Enter percentage of student : "))
    res= name + " " + str(rollno) + " " + str(per) + "\n"
    fout.write(res)

fout.close()
