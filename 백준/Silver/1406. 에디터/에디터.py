from collections import deque
import sys
q=deque(sys.stdin.readline().rstrip())
p=deque()
n=int(sys.stdin.readline())
point=len(q)
cnt=len(q)
for _ in range(n):
    command=list(sys.stdin.readline().rstrip().split())
    if command[0]=='P':
        q.append(command[1])
    elif command[0]=='L':
        if q:
            p.appendleft(q.pop())
    elif command[0] == 'D':
        if p:
            q.append(p.popleft())
    elif command[0] =='B':
        if q:
            q.pop()
    #print(q,p)
q.extend(p)
print(''.join(q))