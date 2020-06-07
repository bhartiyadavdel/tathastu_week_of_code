onary"))
dictionary1= dict()
for i in range(x):
    key=input("enter the key for index "+str(i+1)+":")
    values=int(input("enter the value for corresponding index :"))
    dictionary1[key]=values
dictionary=sorted(dictionary1.values(),reverse=True)
print("second largest element is",dictionary[1])    
