try:
    f=open("Student.txt","r")
except:
    print("file not found")
else:
    print("File found")
finally:
    print("Completed")

