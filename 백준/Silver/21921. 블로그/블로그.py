from collections import deque
n,x=map(int,input().split())

num=list(map(int,input().split()))
q=deque(num[:x])
d=sum(num[:x])
answer=sum(num[:x])
num=deque(num[x:])
cnt=1
while num:
    a=q.popleft()
    b=num.popleft()
    q.append(b)
    d=d-a+b
    if d==answer:
        cnt+=1
    elif d>answer:
        answer=d
        cnt=1

if answer==0:
    print('SAD')
    exit()
else:
    print(answer)
    print(cnt)

