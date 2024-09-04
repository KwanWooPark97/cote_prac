from collections import deque
n,m=map(int,input().split())

adj=[[] for _ in range(n)]
adj_2=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    adj[b-1].append(a-1)
    adj_2[a-1].append(b-1)

answer=0
l=[]
for i in range(n):
    visited = [0] * n
    q=deque([])
    q.append(i)
    while q:
        now=q.popleft()
        for j in adj[now]:
            if visited[j]==0:
                visited[j]=1
                q.append(j)
    l.append(visited)
l_2=[]
for i in range(n):
    visited = [0] * n
    q=deque([])
    q.append(i)
    while q:
        now=q.popleft()
        for j in adj_2[now]:
            if visited[j]==0:
                visited[j]=1
                q.append(j)
    l_2.append(visited)
answer=0
for i in range(n):
    if sum(l[i])+sum(l_2[i])==n-1:
        answer+=1
print(answer)