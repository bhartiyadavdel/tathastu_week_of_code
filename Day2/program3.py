x=int(input("enter the value of N:"))
for i in range(x):
    print(" "*i+"*"+"  "*(x-1-i)+"*")
for i in range(x):
    print(" "*(x-1-i)+"*"+"  "*i+"*")    
