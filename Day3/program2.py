def permutation(List,String=""):
    Set=set(List)
    stringList=[]
    if len(Set)==1:
        String+="".join(List)
        return list([String])
    for x in Set:
        List1=list(List)
        S=String+x;
        List1.remove(x)
        stringList.extend(permutation(List1,S))
    return stringList  
string=input("enter the string:")
List = permutation(list(string))
print("all the permutation of the given string is:"+",".join(List))          
