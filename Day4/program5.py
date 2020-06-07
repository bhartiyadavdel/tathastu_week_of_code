n=int(input("enter the no of votes : "))
votes=[]
for i in range(n):
    votes.append(input("enter the name of the candidate : "))
vote=[]
for name in votes:
    vote.append((name,votes.count(name)))
vote.sort(key=lambda x:x[0])
print("candidates who won the vote is :",vote[-1])
