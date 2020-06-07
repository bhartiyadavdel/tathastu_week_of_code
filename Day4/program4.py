x=int(input("enter the size of the dictionary"))
dictionary1= dict()
for i in range(x):
    key=input("enter the key for index "+str(i+1)+":")
    value=int(input("enter the value for corresponding index :"))
    dictionary1[key]=value
def dup(dictionary):
    dupdict= dict()
    for key,value in dictionary.items():
        if value not in dupdict.values():
            dupdict[key]=value
    return dupdict        
print("dictionary after removing values is",dup(dictionary1))
