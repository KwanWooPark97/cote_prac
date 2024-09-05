from collections import deque

n,w,l=map(int,input().split())
q=deque([0]*w,maxlen=w)
truck=deque(map(int,input().split()))
cnt=0
while truck:
    if q[0] != 0:
        q.append(0)
    else:
        q.rotate(-1)
    if sum(q)+truck[0]<=l:
        q[-1]=truck.popleft()
    cnt+=1
while sum(q)!=0:
    cnt+=1
    q.append(0)
print(cnt)