x=int(input("enter the value of n"))
for i in range(x):
    print("*"*(x-i)+"  "*i+"*"*(x-i))
for i in range(2,x+1):
    print("*"*i+"  "*(x-i)+"*"*(i))    
