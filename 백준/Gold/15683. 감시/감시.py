n,m=map(int,input().split())

cctv=[]
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
wall=[]
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            cctv.append((i,j))
        if board[i][j]==6:
            wall.append([i,j])
answer=1e9
def right(i,v):
    for k in range(i[1], m):
        if board[i[0]][k] == 6:
            break
        v[i[0]][k] = 1
    return v
def left(i,v):
    for k in range(i[1], -1, -1):
        if board[i[0]][k] == 6:
            break
        v[i[0]][k] = 1
    return v
def up(i,v):
    for k in range(i[0], -1, -1):
        if board[k][i[1]] == 6:
            break
        v[k][i[1]] = 1
    return v
def down(i,v):
    for k in range(i[0], n):
        if board[k][i[1]] == 6:
            break
        v[k][i[1]] = 1
    return v
def check(pos):
    visited=[[0]*m for _ in range(n)]
    for i in wall:
        visited[i[0]][i[1]]=1
    for i in pos.keys():
        visited[i[0]][i[1]]=1
        if board[i[0]][i[1]]==1:
            if pos[i]==0:
                visited=right(i,visited)
            elif pos[i]==1:
                visited=down(i,visited)
            elif pos[i]==2:
                visited=left(i,visited)
            elif pos[i]==3:
                visited=up(i,visited)
        elif board[i[0]][i[1]]==2:
            if pos[i]==0:
                visited=right(i,visited)
                visited=left(i,visited)
            else:
                visited=up(i,visited)
                visited=down(i,visited)
        elif board[i[0]][i[1]]==3:
            if pos[i]==0:
                visited=right(i,visited)
                visited=up(i,visited)
            elif pos[i]==1:
                visited=right(i,visited)
                visited=down(i,visited)
            elif pos[i]==2:
                visited=down(i,visited)
                visited=left(i,visited)
            elif pos[i]==3:
                visited=left(i,visited)
                visited=up(i,visited)
        elif board[i[0]][i[1]]==4:
            if pos[i]==0:
                visited=right(i,visited)
                visited=up(i,visited)
                visited = left(i, visited)
            elif pos[i]==1:
                visited = up(i, visited)
                visited=right(i,visited)
                visited=down(i,visited)
            elif pos[i]==2:
                visited = right(i, visited)
                visited=down(i,visited)
                visited=left(i,visited)
            elif pos[i]==3:
                visited = down(i, visited)
                visited=left(i,visited)
                visited=up(i,visited)
        elif board[i[0]][i[1]] == 5:
            visited = down(i, visited)
            visited = left(i, visited)
            visited = up(i, visited)
            visited = right(i, visited)
    c=0
    for i in range(n):
        c+=visited[i].count(0)
        '''print(*visited[i])
    print('*'*20)'''
    return c

def dfs(pos,dep):
    if len(pos.keys())==len(cctv):
        global answer
        answer=min(answer,check(pos))
        return

    for i in range(dep,len(cctv)):
        if board[cctv[i][0]][cctv[i][1]]==1:
            for j in range(4):
                pos[cctv[i]]=j
                dfs(pos,i+1)
                pos.pop(cctv[i])
        elif board[cctv[i][0]][cctv[i][1]]==2:
            for j in range(2):
                pos[cctv[i]]=j
                dfs(pos,i+1)
                pos.pop(cctv[i])
        elif board[cctv[i][0]][cctv[i][1]]==3:
            for j in range(4):
                pos[cctv[i]]=j
                dfs(pos,i+1)
                pos.pop(cctv[i])
        elif board[cctv[i][0]][cctv[i][1]]==4:
            for j in range(4):
                pos[cctv[i]]=j
                dfs(pos,i+1)
                pos.pop(cctv[i])
        elif board[cctv[i][0]][cctv[i][1]]==5:
            pos[cctv[i]]=i
            dfs(pos,i+1)
            pos.pop(cctv[i])

dfs(dict(),0)
print(answer)