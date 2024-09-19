from collections import deque
n,l,r=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
def bfs(y,x):
    q = deque([])
    q.append([y,x])
    visited[y][x] = 1
    path=[[y,x]]
    dy=[0,0,-1,1]
    dx=[1,-1,0,0]
    while q:
        y,x = q.popleft()
        for i in range(4):
            new_y=y+dy[i]
            new_x=x+dx[i]
            if 0<=new_y<n and 0<=new_x<n and visited[new_y][new_x]==0 and l<=abs(board[y][x]-board[new_y][new_x])<=r:
                path.append([new_y,new_x])
                q.append([new_y,new_x])
                visited[new_y][new_x]=1
    return path
day=0
while True:
    visited=[[0]*n for _ in range(n)]
    cnt=0
    temp=[]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                path=bfs(i,j)
                if len(path)>1:
                    temp.append(path)
    for i in range(len(temp)):
        a=0
        for k in temp[i]:
            a+=board[k[0]][k[1]]
        a=a//len(temp[i])
        for k in temp[i]:
            board[k[0]][k[1]]=a
        cnt+=1
    if cnt==0:
        break
    else:
        day+=1
print(day)