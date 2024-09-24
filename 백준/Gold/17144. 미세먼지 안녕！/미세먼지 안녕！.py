from collections import deque
import copy
r,c,t=map(int,input().split())
board=[]
for i in range(r):
    board.append(list(map(int,input().split())))
for i in range(r):
    if board[i][0]==-1:
        cleaner=i
        break
dy=[0,-1,1,0]
dx=[-1,0,0,1]
for _ in range(t):
    new_board=copy.deepcopy(board)
    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                cnt=0
                for k in range(4):
                    new_y = i + dy[k]
                    new_x = j + dx[k]
                    if 0 <= new_y < r and 0 <= new_x < c and board[new_y][new_x]!=-1:
                        new_board[new_y][new_x]+=board[i][j]//5
                        cnt+=1
                new_board[i][j]-=(board[i][j]//5)*cnt
    new_board[cleaner].insert(0,-1)
    new_board[cleaner][1]=0
    temp=new_board[cleaner].pop()
    for i in range(cleaner)[::-1]:
        new_board[i][-1],temp=temp,new_board[i][-1]
    new_board[0].insert(-1,temp)
    temp=new_board[0].pop(0)
    for i in range(cleaner-1):
        new_board[i+1][0],temp=temp,new_board[i+1][0]

    new_board[cleaner+1].insert(0, -1)
    new_board[cleaner+1][1] = 0
    temp = new_board[cleaner+1].pop()
    for i in range(cleaner+2,r):
        new_board[i][-1], temp = temp, new_board[i][-1]
    new_board[-1].insert(-1, temp)
    temp = new_board[-1].pop(0)
    for i in range(r-2,cleaner+1,-1):
        new_board[i][0], temp = temp, new_board[i][0]

    board=new_board
answer=0
for i in range(r):
    #print(*board[i])
    answer+=sum(board[i])
print(answer+2)
