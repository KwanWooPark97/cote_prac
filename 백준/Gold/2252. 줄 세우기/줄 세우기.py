from collections import deque

n,m=map(int,input().split())

adj=[[] for _ in range(n)]
visited=[0]*n
for _ in range(m):
    a, b = map(int,input().split())
    adj[a-1].append(b-1)
    visited[b-1]+=1

q=deque([])
for i in range(n):
    if visited[i]==0:
        q.append(i)
answer=[]
while q:
    now=q.popleft()
    answer.append(now)
    for j in adj[now]:
        visited[j]-=1
        if visited[j]==0:
            q.append(j)

for i in answer:
    print(i+1, end=' ')