from collections import deque
import heapq
n=int(input())
board=[]

for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            sy,sx=i,j

def bfs(y,x,s):
    visited=[[0]*n for _ in range(n)]
    q = deque([])
    q.append([y,x])
    visited[y][x] = 1
    dy=[0,-1,1,0]
    dx=[-1,0,0,1]
    path=[]
    while q:
        y,x = q.popleft()
        for i in range(4):
            new_y=y+dy[i]
            new_x=x+dx[i]
            if 0<=new_y<n and 0<=new_x<n and visited[new_y][new_x]==0 and board[new_y][new_x]<=s:
                visited[new_y][new_x] = visited[y][x]+1
                if 0<board[new_y][new_x]<s:
                    heapq.heappush(path,[visited[y][x],new_y,new_x])
                q.append([new_y,new_x])
    return path
cnt=0
s=2
answer=0
while True:
    re=bfs(sy,sx,s)
    if len(re)==0:
        print(answer)
        break
    else:
        cnt+=1
        if cnt==s:
            s+=1
            cnt=0
        cost,y,x=heapq.heappop(re)
        board[y][x]=9
        board[sy][sx]=0
        sy,sx=y,x
        answer+=cost