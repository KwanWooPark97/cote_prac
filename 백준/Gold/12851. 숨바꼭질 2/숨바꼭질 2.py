import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
visited=[0]*100001
def bfs(x,y):
    q=deque([x])
    visited[x]=1
    cnt=0
    while q:
        new_x=q.popleft()
        for i in (new_x*2,new_x+1,new_x-1):
            if 0<=i<=100000 and (visited[i]==0 or visited[i]==visited[new_x]+1):
                if i==y:
                    cnt+=1
                visited[i]=visited[new_x]+1
                q.append(i)
    return cnt
if n==m:
    print(0)
    print(1)
else:
    cnt=bfs(m,n)
    print(visited[n]-1)
    print(cnt)