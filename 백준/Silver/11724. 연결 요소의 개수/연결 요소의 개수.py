import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a][b]=graph[b][a]=1

def bfs(start,cnt):
    q=deque([start])
    visited[start]=cnt
    while q:
        node=q.popleft()
        for i in range(len(graph[0])):
            if graph[node][i]==1 and visited[i]==0:
                visited[i]=cnt
                q.append(i)
cnt=1
for i in range(1,n+1):
    if visited[i]==0:
        bfs(i,cnt)
        cnt+=1

print(cnt-1)