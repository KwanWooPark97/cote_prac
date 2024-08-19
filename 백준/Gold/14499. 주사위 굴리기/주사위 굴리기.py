import sys
n,m,y,x,k=map(int,sys.stdin.readline().split())

board=[]

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

move=list(map(int,sys.stdin.readline().split()))

ran={key:0 for key in range(1,7)}

dice=[1 ,6, 3, 4, 5, 2]

for i in range(len(move)):
    if move[i]==1:
        new_x=x+1
        if new_x>=m:
            continue
        if 0<=new_x<m:
            dice = dice[2:4][::-1] + dice[:2] + dice[4:]
            if board[y][new_x] != 0:
                ran[dice[1]]=board[y][new_x]
                board[y][new_x]=0
            else:
                board[y][new_x]=ran[dice[1]]
            x=new_x
            print(ran[dice[0]])

    elif move[i]==2:
        new_x = x - 1
        if new_x<0:
            continue
        if 0 <= new_x < m:
            dice = dice[2:4] + dice[:2][::-1] + dice[4:]
            if board[y][new_x]!=0:
                ran[dice[1]]= board[y][new_x]
                board[y][new_x] = 0
            else:
                board[y][new_x]=ran[dice[1]]
            x = new_x
            print(ran[dice[0]])
    elif move[i] == 3:
        new_y = y - 1
        if new_y<0:
            continue
        if 0 <= new_y < n:
            dice = dice[4:] + dice[2:4] + dice[:2][::-1]
            if board[new_y][x] != 0:
                ran[dice[1]] = board[new_y][x]
                board[new_y][x] = 0
            else:
                board[new_y][x]=ran[dice[1]]
            y = new_y
            print(ran[dice[0]])
    elif move[i] == 4:
        new_y = y + 1
        if new_y >=n:
            continue
        if 0 <= new_y < n:
            dice = dice[4:][::-1] + dice[2:4] + dice[:2]
            if board[new_y][x] != 0:
                ran[dice[1]] = board[new_y][x]
                board[new_y][x] = 0
            else:
                board[new_y][x]=ran[dice[1]]
            y = new_y
            print(ran[dice[0]])
