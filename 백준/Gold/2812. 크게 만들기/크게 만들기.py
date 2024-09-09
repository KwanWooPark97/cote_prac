import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())

num=list(map(str,sys.stdin.readline().rstrip()))
stack=deque()

for i in range(n):
    while stack and m>0:
        if stack[-1] < num[i]:
            stack.pop()
            m-=1
        else:
            break
    stack.append(num[i])

if m!=0:
    stack=list(stack)[:-m]
print(int(''.join(stack)))

