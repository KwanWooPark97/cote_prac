import sys
from collections import deque
n=int(input())

r=deque(map(int,sys.stdin.readline().split()))
q=[]
answer=0
while r:
    q.append(r.popleft())
    q.append(r.popleft())
    if q==q[::-1]:
        answer+=1
        q=[]

if q:
    if q==q[::-1]:
        answer+=1
    else:
        answer=0
if answer==0:
    answer=-1

print(answer)