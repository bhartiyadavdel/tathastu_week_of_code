def checkprime(num):
    if(num>1):
        for i in range(2,num//2):
            if(num%i)==0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime no.")
    else:
        print(num,"isn't a prime no.")
def checkodd(num):
    if(num%2 == 0):
        print("yes it is an even  no.") 
    else:
        print("it  is a odd no.") 
def checkpallindrone(n):          
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
def checkarmstrong(n):
    d=n
    c=str(n)
    l=list(c)
    s=len(l)
    sum=0
    while n>0:
        r=n%10
        h=r**s
        sum=sum+h
        n=n/10
    if(sum == d):
        print("yes also a armstrong") 
    else:
        print("not a armstrong")
def check():
    x=int(input("enter the no "))                      
    checkprime(x)
    checkodd(x)
    checkpallindrone(x)
    checkarmstrong(x)
check()
    
