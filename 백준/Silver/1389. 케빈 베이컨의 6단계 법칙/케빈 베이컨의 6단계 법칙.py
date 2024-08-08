from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())


board=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    board[a-1].append(b-1)
    board[b-1].append(a-1)

def bfs(x):
    q=deque([x])
    visited = [0] * n
    visited[x]=1
    while q:
        now=q.popleft()
        for i in board[now]:
            if visited[i]==0:
                q.append(i)
                visited[i]=visited[now]+1
    return visited

cnt=[]
for i in range(n):
    re=bfs(i)
    cnt.append(sum(re))
print(cnt.index(min(cnt))+1)