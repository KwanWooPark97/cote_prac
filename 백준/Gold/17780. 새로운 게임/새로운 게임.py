n,k=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

mal=[[[] for a in range(n)] for b in range(n)]
pos=[]
for i in range(k):
    y,x,d=map(int,input().split())
    mal[y-1][x-1].append(i)
    pos.append([y-1,x-1,d])
answer=1
flag=False
while answer<1001:
    for i in range(len(pos)):
        y,x,d=pos[i]
        if len(mal[y][x])>=2 and mal[y][x][0] != i:
            continue
        if d==1: #오른쪽 움직임
            new_x = x + 1
            if new_x >= n or board[y][new_x] == 2: #움직인곳 파란색
                pos[i][2] = 2
                new_x = x - 1
                if new_x < 0 or board[y][new_x] == 2: #바꾼곳도 파란색
                    continue
            for j in mal[y][x]:
                pos[j] = [y, new_x, pos[j][2]]
            if board[y][new_x]==1:
                mal[y][x] = mal[y][x][::-1]
            mal[y][new_x].extend(mal[y][x])
            mal[y][x] = []

            x = new_x
        elif d==2: #왼쪽 움직임
            new_x = x - 1
            if new_x < 0 or board[y][new_x] == 2:  # 움직인곳 파란색
                pos[i][2] = 1
                new_x = x + 1
                if new_x >= n or board[y][new_x] == 2:  # 바꾼곳도 파란색
                    continue
            for j in mal[y][x]:
                pos[j] = [y, new_x, pos[j][2]]
            if board[y][new_x] == 1:
                mal[y][x] = mal[y][x][::-1]
            mal[y][new_x].extend(mal[y][x])
            mal[y][x] = []


            x=new_x
        elif d==3:
            new_y = y - 1
            if new_y < 0 or board[new_y][x] == 2:  # 움직인곳 파란색
                pos[i][2] = 4
                new_y = y + 1
                if new_y >= n or board[new_y][x] == 2:  # 바꾼곳도 파란색
                    continue
            for j in mal[y][x]:
                pos[j] = [new_y, x, pos[j][2]]
            if board[new_y][x] == 1:
                mal[y][x] = mal[y][x][::-1]
            mal[new_y][x].extend(mal[y][x])
            mal[y][x] = []


            y = new_y
        elif d==4:
            new_y = y + 1
            if new_y >= n or board[new_y][x] == 2:  # 움직인곳 파란색
                pos[i][2] = 3
                new_y = y - 1
                if new_y < 0 or board[new_y][x] == 2:  # 바꾼곳도 파란색
                    continue

            for j in mal[y][x]:
                pos[j] = [new_y, x, pos[j][2]]
            if board[new_y][x] == 1:
                mal[y][x] = mal[y][x][::-1]
            mal[new_y][x].extend(mal[y][x])
            mal[y][x] = []
            y=new_y

        if len(mal[y][x])>=4:
            flag=True
            break
    else:
        answer+=1

    if flag:
        break
if answer>1000:
    print(-1)
else:
    print(answer)