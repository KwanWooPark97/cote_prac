import heapq
import sys
n,m=map(int,sys.stdin.readline().split())

adj=[[] for i in range(n)]

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    adj[a-1].append((b-1,c))
    adj[b-1].append((a-1,c))

visited=[1e9]*n
visited[0]=0

q=[]

heapq.heappush(q,[0,0])

while q:
    cost,now=heapq.heappop(q)
    if now==n-1:
        continue
    if cost>visited[-1]:
        continue
    for new,val in adj[now]:
        if new!=0 and visited[new]>cost+val:
            visited[new]=cost+val
            heapq.heappush(q,[cost+val,new])

print(visited[-1])