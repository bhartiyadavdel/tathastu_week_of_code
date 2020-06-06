def intersection(List1,List2):
    templist=[]
    for i in List1:
        if i in List2:
            templist.append(i)
    return templist
x1=int(input("enter the size of List 1"))
List1=[]
print("enter the elements of list1")
for i in range(x1):
    List1.append(input())
x2=int(input("enter the size of list 2"))
List2=[]
for i in range(x2):
    List2.append(input())
print("Intersection of both the Lists is: ",intersection(List1,List2))                   
