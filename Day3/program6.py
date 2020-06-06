def Sum(List,size,sum):
    slist=[]
    if size == 1:
        for x in List:
            slist.append(sum+x)
        return slist
    list1=List.copy()
    for i in List:
        list1.remove(i)
        slist.extend(Sum(list1,size-1,sum+i))
    return slist        
def summation(List,size):
    slist=List.copy()
    for i in range(2,size+1):
        slist.extend(Sum(List,i,0))
    num=1
    while True:
        if num not in slist:
            print("least number whose summation is not present is ",num)
            break
        num+=1
List=[]        
size=int(input("enter the size of the list"))
print("enter the elements of the list")
for i in range(size):
    List.append(int(input()))
summation(List,size)    
