x=int(input("enter the value of n"))
for i in range(x):
    print((str(x-i)+"*")*(x-i-1)+str(x-i))
for i in range(1,x+1):    
    print((str(i)+"*")*(i-1)+str(i))
