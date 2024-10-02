import sys
from collections import deque
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
q=deque([0])
start=a[0]
answer=[]
cnt=1
for i in range(1,n):
    if a[i]!=start:
        answer.extend([i+1]*cnt)
        start=a[i]
        cnt=1
    else:
        cnt+=1

if cnt!=0:
    answer.extend([-1]*cnt)

print(*answer)