import sys
from collections import deque
n=int(sys.stdin.readline())
board=[[0]*n for i in range(n)]
k=int(sys.stdin.readline())
for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    board[a-1][b-1]=1
board[0][0]=2
m=int(sys.stdin.readline())

times=[]
for _ in range(m):
    times.append(list(sys.stdin.readline().split()))
dir=0
def move(y,x):
    global cnt,dir,flag

    if dir%4==0:
        cnt+=1
        new_x=x+1
        if new_x>=len(board) or new_x<0 or [y,new_x] in body:
            print(cnt)
            flag=False
            return
        if board[y][new_x]==1:
            board[y][new_x] = 0
            body.appendleft([y,new_x])
        else:
            body.pop()
            body.appendleft([y,new_x])

    elif dir%4==1:
        cnt+=1
        new_y=y+1
        if new_y>=len(board) or new_y<0 or [new_y,x] in body:
            print(cnt)
            flag=False
            return
        if board[new_y][x]==1:
            board[new_y][x] = 0
            body.appendleft([new_y,x])
        else:
            body.pop()
            body.appendleft([new_y,x])

    elif dir%4==2:
        cnt+=1
        new_x=x-1
        if new_x>=len(board) or new_x<0 or [y,new_x] in body:

            print(cnt)
            flag=False
            return
        if board[y][new_x]==1:
            board[y][new_x] = 0
            body.appendleft([y,new_x])
        else:
            body.pop()
            body.appendleft([y,new_x])

    elif dir%4==3:
        cnt+=1
        new_y=y-1
        if new_y>=len(board) or new_y<0 or [new_y,x] in body:
            print(cnt)
            flag=False
            return
        if board[new_y][x]==1:
            board[new_y][x] = 0
            body.appendleft([new_y,x])
        else:
            body.pop()
            body.appendleft([new_y,x])
    return flag

body=deque([[0,0]])
ca=0
cnt=0
t=0
flag=True
while flag:
    move(body[0][0],body[0][1])
    if cnt >= int(times[t][0]) and cnt <=int(times[-1][0]):
        if times[t][1]=='D':
            dir+=1
        elif times[t][1]=='L':
            dir-=1

        if t<len(times)-1:
            t+=1