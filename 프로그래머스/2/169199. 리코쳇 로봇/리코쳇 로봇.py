from collections import deque
def solution(board):
    answer = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited=[[0]*len(board[0]) for _ in range(len(board))]
    real_board=[]
    for i in board:
        real_board.append(list(map(str,i)))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if real_board[i][j]=='.':
                real_board[i][j]=0
            elif real_board[i][j]=='D':
                real_board[i][j]=1
            elif real_board[i][j]=='R':
                real_board[i][j]=0
                sy,sx=i,j
            elif real_board[i][j]=='G':
                real_board[i][j]=0
                gy,gx=i,j
    
    def move(y,x,dx,dy):
        while 0<=x+dx<len(real_board[0]) and 0<=y+dy<len(real_board) and real_board[y+dy][x+dx]==0:
            x+=dx
            y+=dy
        return y,x
    def bfs(y,x,gy,gx):
        q=deque()
        q.append([y,x])
        visited[y][x]=1
        cnt=0
        while q:
            cnt+=1
            y,x=q.popleft()
            for i in range(4):
                yy,xx=move(y,x,dx[i],dy[i])
                if visited[yy][xx]==0:
                    #yy,xx=move(y,x,dx[i],dy[i])
                    if yy==gy and xx==gx:
                        return visited[y][x],True
                    elif visited[yy][xx]>=visited[y][x]:
                        continue
                    #visited[y][x]=1
                    visited[yy][xx]=visited[y][x]+1
                    
                    q.append([yy,xx])
        return visited[yy][xx],False
    
    
        
    answer,goal=bfs(sy,sx,gy,gx)
    if goal:
        return answer
    else:
        return -1