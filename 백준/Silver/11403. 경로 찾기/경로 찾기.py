from collections import deque
n=int(input())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

adj=[[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            adj[i].append(j)

answer=[]
for i in range(n):
    visited=[0]*n
    q=deque([])
    q.append(i)
    while q:
        now=q.popleft()
        for k in adj[now]:
            if visited[k]==0:
                visited[k]=1
                q.append(k)

    answer.append(visited)

for i in range(n):
    print(*answer[i])