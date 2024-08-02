import sys
from collections import deque
com=int(input())
node_num=int(input())

node=[[0]*(com+1) for _ in range(com+1)]
visited=[0]*(com+1)
for i in range(node_num):
    a,b=map(int,input().split())
    node[a][b]=node[b][a]=1
cnt=0
def bfs(i):
    global cnt
    visited[i]=1
    q=deque([i])
    while q:
        num=q.popleft()
        for j in range(2,len(node[0])):
            if node[num][j]==1 and visited[j]==0:
                q.append(j)
                visited[j]=1
                cnt+=1

bfs(1)
print(cnt)
