import sys
from collections import deque
t=int(sys.stdin.readline())

for _ in range(t):
    answer = 0
    q=[]
    day=int(sys.stdin.readline())
    price=deque(list(map(int,sys.stdin.readline().split()))[::-1])
    q.append(price.popleft())
    while price:
        a=price.popleft()
        if a>q[0] and len(q)>1:
            answer+=q[0]*len(q[1:])-sum(q[1:])
            q=[a]
        elif a>q[0] and len(q)==1:
            q = [a]
        else:
            q.append(a)
    if len(q)>1:
        answer += q[0] * len(q[1:]) - sum(q[1:])
    print(answer)