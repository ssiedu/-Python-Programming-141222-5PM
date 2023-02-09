list1=["apple\n","banana\n","orange\n","kiwi\n"]
fout=open("list.txt","w")
fout.writelines(list1)
fout.close()
