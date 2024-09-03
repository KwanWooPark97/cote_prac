from collections import deque

k=int(input())

w,h=map(int,input().split())

visited=[[[False for i in range(40)] for j in range(w)]for _ in range(h)]

board=[]

for _ in range(h):
    board.append(list(map(int,input().split())))

q=deque([])
q.append([[0,0],k])
visited[0][0][k]=True
dist=[[[0 for i in range(40)] for j in range(w)]for _ in range(h)]
kh=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
while q:
    pos,horse=q.popleft()
    y,x=pos
    if y==h-1 and x==w-1:
        break

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_x < w and 0 <= new_y < h and board[new_y][new_x] == 0 and visited[new_y][new_x][horse]==False:
            visited[new_y][new_x][horse] = True
            dist[new_y][new_x][horse]=dist[y][x][horse]+1
            q.append([[new_y, new_x], horse])
    if horse !=0:
        for i in range(8):
            new_y=y+kh[i][0]
            new_x=x+kh[i][1]
            if 0<=new_x<w and 0<=new_y<h and board[new_y][new_x]==0 and (visited[new_y][new_x][horse-1]==False):
                visited[new_y][new_x][horse-1] = True
                dist[new_y][new_x][horse-1] = dist[y][x][horse] + 1
                q.append([[new_y, new_x], horse-1])

answer=1e9
for i in dist[-1][-1]:
    if i!=0:
        answer=min(answer,i)
if w==1 and h==1:
    print(0)
elif answer==1e9:
    print(-1)

else:
    print(answer)