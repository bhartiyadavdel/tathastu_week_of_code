def dupList(List):
    dlist=[]
    for x  in List:
        if x not in dlist:
            dlist.append(x)
    return dlist
size=int(input("enter the size of the list"))
print("enter the elements of the list")
List=[]
for i in range(size):
    List.append(input())
print("list after removing duplicate elements is",dupList(List))

