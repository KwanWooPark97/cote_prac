from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    data=list(map(int,input()))
    graph.append(data)




dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    que=deque()
    que.append((y,x))
    while que:
        y,x=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny <0 or nx>m-1 or ny>n-1:
                continue
            elif graph[ny][nx]==0:
                continue
            elif graph[ny][nx]==1:
                graph[ny][nx]=graph[y][x]+1
                #graph[y][x] = 0
                que.append((ny,nx))

    return graph[n-1][m-1]
print(bfs(0,0))