import heapq
import sys
INF = int(1e9)

N, D = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    start, end, length = map(int,sys.stdin.readline().split())
    if end > D or (end-start)<=length:
        continue
    graph[start].append((end,length))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        cost, now = heapq.heappop(q)
        if cost > distance[now]:
            continue
        for i in graph[now]:
            now_dist= cost +i[1]
            if now_dist < distance[i[0]]:
                distance[i[0]] = now_dist
                heapq.heappush(q,(now_dist, i[0]))
dijkstra(0)
print(distance[D])