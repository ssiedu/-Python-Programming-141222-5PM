fout=open("myfile1.txt","w")
for i in range(5):
    name=input("Enter Name of student : ")
    fout.write(name+"\n")
fout.close()
