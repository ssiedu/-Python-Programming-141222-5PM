def list1(*data):
    print(data)
    print("data[1] : ",data[1])


list1(11,22,33,44)


def kwarg(**data):
    print(data)
    print("first number : ",data["fnum"])


kwarg(fnum=12,snum=13,tnum=15)
