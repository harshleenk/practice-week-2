lis=[]
n=int(input("Enter the number of elements of dict: "))
for i in range(0,n):
    x=int(input("enter the elements of dict: "))
    lis.append(x)
print("list is: ")
sq={}
for i in range(0,n):
    sq[i]=[i*i]
print(sq)