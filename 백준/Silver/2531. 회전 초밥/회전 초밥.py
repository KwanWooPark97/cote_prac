import sys
from collections import deque,Counter
n,d,k,c=map(int,sys.stdin.readline().split())

q=[]

for i in range(n):
    q.append(int(sys.stdin.readline()))
q.extend(q)
p=deque(q[:k])
answer=0
for i in range(k,n+k+1):
    a=set(p)
    a.add(c)
    answer=max(answer,len(a))
    if answer==d:
        break
    p.popleft()
    p.append(q[i])

print(answer)