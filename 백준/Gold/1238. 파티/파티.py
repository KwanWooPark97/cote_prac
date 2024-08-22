import sys
from collections import deque
n,m,x=map(int,sys.stdin.readline().split())

adj=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    adj[a].append([b,c])



answer=[0]*(n+1)
for k in range(1,n+1):
    q=deque()
    visited = [1e9] * (n + 1)
    visited[k] = 0
    q.append([0,k])
    while q:
        cost,node=q.popleft()
        if visited[node]<cost:
            continue
        for i,j in adj[node]:
            if visited[i]>j+cost:
                q.append([j+cost,i])
                visited[i]=j+cost
    answer[k]=visited[x]

q=deque()
visited = [1e9] * (n + 1)
visited[x] = 0
q.append([0,x])

while q:
    cost, node = q.popleft()
    if visited[node] < cost:
        continue
    for i, j in adj[node]:
        if visited[i] > j + cost:
            q.append([j + cost, i])
            visited[i] = j + cost

for idx,val in enumerate(visited):
    answer[idx]+=val

print(max(answer[1:]))