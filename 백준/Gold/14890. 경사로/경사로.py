n,l=map(int,input().split())

board=[]

for i in range(n):
    board.append(list(map(int,input().split())))

for i in zip(*board):
    board.append(list(i))
def up(y,x):
    if x<l:
        return False
    start=board[y][x-l]
    for i in range(x-l,x):
        if visited[i]==1 and board[i]!=start:
            return False
    else:
        for i in range(x-l,x):
            visited[i]=1
    return True

def down(y,x):
    if x+l>n:
        return False
    start=board[y][x]
    for i in range(x,x+l):
        if visited[i]==1 and board[i]!=start:
            return False
    else:
        for i in range(x,x+l):
            visited[i]=1
    return True

answer=0
for i in range(len(board)):
    visited=[0]*n
    height=board[i][0]
    for j in range(n):
        if board[i][j]>height:
            if board[i][j]-height<2 and up(i,j):
                height=board[i][j]
            else:
                break
        elif board[i][j]<height:
            if height-board[i][j]<2 and down(i,j):
                height=board[i][j]
            else:
                break
    else:
        answer+=1
print(answer)


