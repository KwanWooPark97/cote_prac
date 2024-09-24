import copy
r,c,m=map(int,input().split())
shark=[]
board=[[[] for _ in range(c)] for _ in range(r)]
for i in range(m):
    y,x,s,d,z=map(int, input().split())
    board[y-1][x-1].append([s,d,z])
def move(board):
    new_board=[[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):

            if len(board[i][j])!=0:
                if board[i][j][0][1]==1 or board[i][j][0][1]==2:
                    cnt=board[i][j][0][0]
                    dd=board[i][j][0][1]
                    cnt=cnt%(2*r-2)
                    now=i
                    while cnt!=0:
                        if now==0:
                            dd=2
                        elif now==r-1:
                            dd=1
                        if dd==1:
                            now-=1
                        else:
                            now+=1

                        cnt-=1
                    new_board[now][j].append([board[i][j][0][0],dd,board[i][j][0][2]])
                else:
                    cnt = board[i][j][0][0]
                    dd = board[i][j][0][1]
                    cnt = cnt % (2 * c - 2)
                    now = j
                    while cnt != 0:
                        if now == 0:
                            dd = 3
                        elif now == c - 1:
                            dd = 4
                        if dd == 4:
                            now -= 1
                        else:
                            now += 1

                        cnt -= 1
                    new_board[i][now].append([board[i][j][0][0], dd, board[i][j][0][2]])
    for i in range(r):
        for j in range(c):
            if len(new_board[i][j])>=2:
                new_board[i][j]=[sorted(new_board[i][j],key=lambda x:x[2])[-1]]
    return new_board



answer=0
for j in range(c):
    for i in range(r):
        if len(board[i][j])!=0:
            answer+=board[i][j][0][2]
            board[i][j]=[]
            break

    board=move(board)

print(answer)


