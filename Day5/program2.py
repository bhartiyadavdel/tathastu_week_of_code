def Max_on_Right(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
size = int(input("Enter the size of the list: "))
List = []    
for i in range(size):
    List.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("The list after replacing each element with max no  on right side is: ",Max_on_Right(List))
