try:
    f=open("abc.txt","r")
except FileNotFoundError:
    print("file not found")

'''else:
    print("file found")
    FileNotFoundError'''
