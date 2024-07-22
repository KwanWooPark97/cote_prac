from collections import deque

n=deque(input())
cnt=0
while n:
    cnt+=1
    for i in str(cnt):
        if len(n)==0:
            break
        if i==n[0]:
            n.popleft()

print(cnt)