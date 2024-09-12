from collections import deque
import copy
n,m=map(int,input().split())

board=[]

for i in range(n):
    board.append(list(map(int,input().split())))
answer=0
start=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            start.append([i,j])
def bfs():
    visited=copy.deepcopy(board)
    q=deque(copy.deepcopy(start))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        y,x=q.popleft()
        for i in range(4):
            now_x=x+dx[i]
            now_y=y+dy[i]
            if 0<=now_y<n and 0<=now_x<m and visited[now_y][now_x]==0:
                visited[now_y][now_x]=2
                q.append([now_y,now_x])

    global answer
    c=0
    for i in range(n):
        c+=visited[i].count(0)
    answer=max(answer,c)
def backtrack(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                backtrack(cnt+1)
                board[i][j]=0

backtrack(0)

print(answer)

