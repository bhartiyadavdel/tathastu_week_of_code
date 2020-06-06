def dup(string):
    Dstring=""
    for x in string:
        if x not in  Dstring:
            Dstring+=x
    return Dstring
st=input("enter th string")
print("string after removing duplicates is :",dup(st))        
