size=int(input("enter the size of the tuple"))
print("enter the elements of the tuple")
tup=[]
for i in range(size):
    tup.append(input())
tup=tuple(tup) 
e=input("enter the element whose count you wish to obtain")   
print("count of the element is",tup.count(e),"times")
