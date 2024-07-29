import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
visited=[0]*100001
def bfs(x,y):
    q=deque([x])
    visited[x]=1
    while q:
        new_x=q.popleft()
        if new_x==y:
            print(visited[new_x]-1)
            return
        for i in (new_x*2,new_x-1,new_x+1):
            if 0<=i<=100000 and visited[i]==0:
                if i==new_x*2:
                    q.appendleft(i)
                    visited[i]=visited[new_x]
                    continue

                visited[i] = visited[new_x]+1
                q.append(i)

if n==m:
    print(0)
else:
    bfs(m,n)