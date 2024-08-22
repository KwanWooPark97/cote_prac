import sys
import heapq
v,e=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())

visited=[1e9]*(v+1)
visited[start]=0

adj=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    adj[a].append([b,c])

q=[]
heapq.heappush(q,[0,start])

while q:
    cost,node=heapq.heappop(q)
    if visited[node]<cost:
        continue
    for i,j in adj[node]:
        if visited[i]>j+cost:
            heapq.heappush(q,[j+cost,i])
            visited[i]=j+cost

for i in visited[1:]:
    if i==1e9:
        print("INF")
    else:
        print(i)