from collections import deque
def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    score=[[500001]*(N+1) for _ in range(N+1)]
    for a,b,c in road:
        if b not in graph[a] or a not in graph[b]:
            graph[a].append(b)
            graph[b].append(a)
        score[a][b]=min(c,score[a][b])
        score[b][a]=min(c,score[b][a])
    
    cost=[1e9]*(N+1)
    cost[0],cost[1]=0,0
    q=deque()
    q.append([1,0])
    while q:
        now,cnt=q.popleft()
        if cost[now]<cnt:
            continue
        for i in graph[now]:
            if cost[i] > cnt+score[now][i]:
                cost[i]=cnt+score[now][i]
                q.append([i,cnt+score[now][i]])
            
    for i in cost[1:]:
        if i<=K:
            answer+=1

    return answer