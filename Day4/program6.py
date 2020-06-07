x= int(input("enter the no of words you want to add in dictionary"))
dict=[]
for i in range(x):
    dict.append(input("enter the word"+str(i+1)+":"))
y=int(input("enter the no of characters you want to add in array"))
arr=[]
for i in range(y):
    arr.append(input("enter the characters : "))
temparr=[]    
for word in dict:
        if set(word).issubset(set(arr)):
            temparr.append(word)
print(" is a possible words are ,".join(temparr)+" is a possible word.")            
