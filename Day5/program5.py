def odd_even(List):
    odd=[]
    even=[]
    for i in List: 
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(odd,reverse=True),sorted(even)
size =  int(input("Enter the number of items you want to enter: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("odd and even no seperately are :",str(odd_even(List)))           
