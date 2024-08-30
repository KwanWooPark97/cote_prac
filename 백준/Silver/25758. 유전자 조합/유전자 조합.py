from itertools import permutations as pb
from collections import Counter
n=int(input())

r=Counter(input().split())
data=[]
for i in r.keys():
    if r[i]>=2:
        data+=[i]*2
    else:
        data+=[i]
a=list(pb(data,2))

answer=set()
for i in a:
    f,s=str(i[0]),str(i[1])
    new=sorted(f[0]+s[1],reverse=True)[0]
    answer.add(new)

answer=list(answer)

print(len(answer))
answer.sort()
for i in answer:
    print(i,end=' ')
