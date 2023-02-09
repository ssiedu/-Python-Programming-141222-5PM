import pickle
fin=open("binary1.dat","rb")
print(fin.readable())
data=pickle.load(fin)
fin.close()
print(data)

