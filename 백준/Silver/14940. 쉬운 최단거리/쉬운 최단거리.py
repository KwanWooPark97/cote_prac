from collections import deque
n,m=map(int,input().split())

board=[]
for i in range(n):
    a=list(map(int,input().split()))
    board.append(a)
    if 2 in a:
        goal_y=i
        goal_x=a.index(2)

def bfs(y,x,board):
    q=deque()
    q.append([y,x])
    visited=[[0]*m for _ in range(n)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        y,x=q.popleft()
        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            if 0<=new_x<m and 0<=new_y<n and board[new_y][new_x]==1 and visited[new_y][new_x]==0:
                q.append([new_y,new_x])
                visited[new_y][new_x]=visited[y][x]+1

    return visited
answer=bfs(goal_y,goal_x,board)

for i in range(n):
    for j in range(m):
        if board[i][j]==1 and answer[i][j]==0:
            print(-1,end=' ')
        else:
            print(answer[i][j],end=' ')
    print('')