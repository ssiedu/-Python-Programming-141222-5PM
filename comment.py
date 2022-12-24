#this is single line comment
print("Single line comment")
"""This is multiline
comment"""
print("Multiline comment")


def fun():
    '''This is docstring comment'''
    a=10
    b=20
    print(a+b)

print(fun.__doc__)
fun()

