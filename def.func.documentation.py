def add(a,b):
    """this is addition func"""
    print("addition: ",a+b)
def sub(a,b):
    """this is subtraction func"""
    print("subtraction: ",a-b)
def mult(c,d):
    """this is multiplication func"""
    e=c*d
    print("multiplication: ",e)

#add(5,7)
#sub(10,4)
#mult(2,3)

x=int(input("a: "))
y=int(input("b: "))

add(x,y)
sub(x,y)
mult(x,y)

print(add.__doc__)
v=sub.__doc__
print(v)
print(mult.__doc__)