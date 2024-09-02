from collections import deque
n,m,t=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

visited=[[0]*m for _ in range(n)]

q=deque([])
q.append([0,0])
visited[0][0]=1
gram=0
while q:
    y,x=q.popleft()
    for i in range(4):
        now_x=x+dx[i]
        now_y=y+dy[i]
        if 0<=now_x<m and 0<=now_y<n and (board[now_y][now_x]==0 or board[now_y][now_x]==2) and visited[now_y][now_x]==0:
            visited[now_y][now_x]=visited[y][x]+1
            if board[now_y][now_x]==2:
                gram=visited[y][x]+((n-1)-now_y)+((m-1)-now_x)
                q.append([now_y,now_x])
            else:
                q.append([now_y,now_x])

'''for i in range(n):
    print(*visited[i])'''
if (visited[-1][-1]==0 or visited[-1][-1]>t) and (gram==0 or gram>t):
    print('Fail')
else:
    if gram>0:
        if visited[-1][-1]==0:
            print(gram)
        else:
            print(min(visited[-1][-1]-1,gram))
    else:
        print(visited[-1][-1]-1)