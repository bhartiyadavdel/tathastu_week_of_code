lsize=int(input("enter the size of the list in which you want to add tuple"))
tsize=int(input("enter the size of each tuple in the list"))
List=[]
for i in range(lsize):
    print("enter the elemnets of tuple",i+1)
    Tuple=[]
    for j in range(tsize):
        Tuple.append(int(input("enter the elements"+str(j+1)+":")))
    List.append(tuple(Tuple))
index=int(input("Enter the index about which you wish to sort the list"))    
List.sort(key = lambda x : x[index])
print("sorted List is:",List)

