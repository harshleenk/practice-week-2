name= input("enter your name: ")
print("the name is: ",name)
subject= input("enter your subject: ")
print("the subject is: ",subject)

def name():
    """"this is a name doc string"""
def subject():
    """"this is a subject doc string"""
print(name.__doc__)
print(subject.__doc__)