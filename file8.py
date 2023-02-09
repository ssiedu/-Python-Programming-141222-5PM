import pickle
file=open("binary1.dat","wb")
x=[11,22,33,44,55]
pickle.dump(x,file)
file.close()
