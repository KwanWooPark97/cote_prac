from collections import deque
import copy
n,m,t=map(int,input().split())
board=[]
for _ in range(n):
    board.append(deque(list(map(int,input().split()))))

dx=[1,-1]
dy=[1,-1]
def bfs(y,x):
    target=board[y][x]
    #new_b=copy.deepcopy(b)
    q=deque()
    q.append([y,x])
    path=[[y,x]]
    while q:
        y,x=q.popleft()
        for i in range(2):
            new_x=x+dx[i]
            if new_x==-1:
                new_x=m-1
            elif new_x==m:
                new_x=0
            if board[y][new_x]==target and [y,new_x] not in path:
                q.append([y,new_x])
                path.append([y,new_x])
        for i in range(2):
            new_y = y + dy[i]
            if new_y == -1 or new_y == n:
                continue
            if board[new_y][x] == target and [new_y,x] not in path:
                q.append([new_y, x])
                path.append([new_y,x])
    return path

for _ in range(t):
    x, d, k_1 = map(int, input().split())
    for i in range(n):
        if (i+1)%x==0:
            if d==0:
                board[i].rotate(k_1)
            else:
                board[i].rotate(-1*k_1)
    cnt = 0
    for i in range(n):

        if sum(board[i])==0:
            continue
        for j in range(m):
            if board[i][j]!=0:
                path=bfs(i,j)
                if len(path)>1:
                    for k in path:
                        board[k[0]][k[1]]=0
                    cnt+=1
    if cnt==0:
        avg=0
        a=0
        for k in range(n):
            for l in range(m):
                if board[k][l]!=0:
                    avg+=board[k][l]
                    a+=1
        if a==0:
            break
        avg=avg/a
        for k in range(n):
            for l in range(m):
                if board[k][l]!=0:
                    if board[k][l]<avg:
                        board[k][l]+=1
                    elif board[k][l]>avg:
                        board[k][l]-=1
    '''for i in range(n):
        print(*board[i])
    print('*'*20)'''


answer=0
for i in range(n):
    #print(*board[i])
    answer+=sum(board[i])
print(answer)