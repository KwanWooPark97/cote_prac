from collections import deque
n,m=map(int,input().split())

graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

cost=[1e9]*n
def bfs():
    q=deque([])
    q.append([0,0])
    cost[0]=0
    while q:
        now,c=q.popleft()
        if cost[now]<c:
            continue
        for i in graph[now]:
            if cost[i]>c+1:
                cost[i]=c+1
                q.append([i,c+1])
bfs()
print(cost.index(max(cost))+1,max(cost),cost.count(max(cost)))