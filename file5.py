list1=[]
fout=open("list1.txt","w")
for i in range(5):
    name=input("Enter name of student : ")
    list1.append(name+"\n")

fout.writelines(list1)
fout.close()
