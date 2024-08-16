import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
board=[]
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

visited=[]
for y in range(n):
    for x in range(m):
        if board[y][x] == "R":
            rx, ry = x, y
        if board[y][x] == "B":
            bx, by = x, y


def move(y,x,dy,dx):
    cnt=0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y+=dy
        x+=dx
        cnt+=1
    return y,x,cnt

def bfs(rx,ry,bx,by):
    q=deque()
    q.append((ry,rx,by,bx,1))
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    visited.append((ry,rx,by,bx))
    while q:
        y,x,by,bx,re=q.popleft()
        if re > 10:
            break
        for i in range(4):
            ry,rx,rcnt=move(y,x,dy[i],dx[i])
            bby,bbx,bcnt=move(by,bx,dy[i],dx[i])

            if board[bby][bbx]=='O':
                continue
            if board[ry][rx]=='O':
                print(re)
                return

            if ry==bby and rx==bbx:
                if rcnt > bcnt:
                    ry-=dy[i]
                    rx-=dx[i]
                else:
                    bby-=dy[i]
                    bbx-=dx[i]
            if (ry,rx,bby,bbx) not in visited:
                visited.append((ry,rx,bby,bbx))
                q.append((ry,rx,bby,bbx,re+1))

    print('-1')

bfs(rx ,ry,bx,by)