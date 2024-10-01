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
        if d==1:
            new_x=x+1
            if new_x<n and board[y][new_x]!=2:
                if len(mal[y][x])>1:
                    a=mal[y][x].index(i)
                    if board[y][new_x]==0:
                        mal[y][new_x].extend(mal[y][x][a:])
                    elif board[y][new_x]==1:
                        mal[y][new_x].extend(mal[y][x][a:][::-1])
                    for j in mal[y][x][a:]:
                        pos[j]=[y,new_x,pos[j][2]]
                    if a!=0:
                        mal[y][x]=mal[y][x][:a]
                    else:
                        mal[y][x]=[]
                else:
                    mal[y][new_x].append(i)
                    pos[i]=[y,new_x,d]
                    mal[y][x] = []
            else:
                d=2
                new_x=x-1
                if new_x<0 or board[y][new_x]==2:
                    pos[i][2]=d
                else:
                    if len(mal[y][x]) > 1:
                        a = mal[y][x].index(i)
                        if board[y][new_x] == 0:
                            mal[y][new_x].extend(mal[y][x][a:])
                        elif board[y][new_x] == 1:
                            mal[y][new_x].extend(mal[y][x][a:][::-1])
                        for j in mal[y][x][a:]:
                            pos[j] = [y, new_x, pos[j][2]]
                        pos[i][2] = d
                        if a != 0:
                            mal[y][x] = mal[y][x][:a]
                        else:
                            mal[y][x] = []
                    else:
                        mal[y][new_x].append(i)
                        pos[i] = [y, new_x, d]
                        mal[y][x] = []
        elif d == 2:
            new_x = x - 1
            if new_x >=0 and board[y][new_x]!=2:
                if len(mal[y][x]) > 1:
                    a = mal[y][x].index(i)
                    if board[y][new_x]==0:
                        mal[y][new_x].extend(mal[y][x][a:])
                    elif board[y][new_x]==1:
                        mal[y][new_x].extend(mal[y][x][a:][::-1])
                    for j in mal[y][x][a:]:
                        pos[j] = [y, new_x, pos[j][2]]
                    if a != 0:
                        mal[y][x] = mal[y][x][:a]
                    else:
                        mal[y][x] = []
                else:
                    mal[y][new_x].append(i)
                    pos[i] = [y, new_x, d]
                    mal[y][x] = []
            else:
                d = 1
                new_x = x + 1
                if new_x >=n or board[y][new_x] == 2:
                    pos[i][2] = d
                else:
                    if len(mal[y][x]) > 1:
                        a = mal[y][x].index(i)
                        if board[y][new_x] == 0:
                            mal[y][new_x].extend(mal[y][x][a:])
                        elif board[y][new_x] == 1:
                            mal[y][new_x].extend(mal[y][x][a:][::-1])
                        for j in mal[y][x][a:]:
                            pos[j] = [y, new_x, pos[j][2]]
                        pos[i][2] = d
                        if a != 0:
                            mal[y][x] = mal[y][x][:a]
                        else:
                            mal[y][x] = []
                    else:
                        mal[y][new_x].append(i)
                        pos[i] = [y, new_x, d]
                        mal[y][x] = []
        elif d == 3:
            new_y = y - 1
            if new_y >=0 and board[new_y][x]!=2:
                if len(mal[y][x]) > 1:
                    a = mal[y][x].index(i)
                    if board[new_y][x]==0:
                        mal[new_y][x].extend(mal[y][x][a:])
                    elif board[new_y][x]==1:
                        mal[new_y][x].extend(mal[y][x][a:][::-1])
                    for j in mal[y][x][a:]:
                        pos[j] = [new_y, x, pos[j][2]]
                    if a != 0:
                        mal[y][x] = mal[y][x][:a]
                    else:
                        mal[y][x] = []
                else:
                    mal[new_y][x].append(i)
                    pos[i] = [new_y, x, d]
                    mal[y][x] = []
            else:
                d = 4
                new_y = y + 1
                if new_y >=n or board[new_y][x] == 2:
                    pos[i][2] = d
                else:
                    if len(mal[y][x]) > 1:
                        a = mal[y][x].index(i)
                        if board[new_y][x] == 0:
                            mal[new_y][x].extend(mal[y][x][a:])
                        elif board[new_y][x] == 1:
                            mal[new_y][x].extend(mal[y][x][a:][::-1])
                        for j in mal[y][x][a:]:
                            pos[j] = [new_y, x, pos[j][2]]
                        pos[i][2] = d
                        if a != 0:
                            mal[y][x] = mal[y][x][:a]
                        else:
                            mal[y][x] = []
                    else:
                        mal[new_y][x].append(i)
                        pos[i] = [new_y, x, d]
                        mal[y][x] = []
        elif d == 4:
            new_y = y + 1
            if new_y < n and board[new_y][x] != 2:
                if len(mal[y][x]) > 1:
                    a = mal[y][x].index(i)
                    if board[new_y][x] == 0:
                        mal[new_y][x].extend(mal[y][x][a:])
                    elif board[new_y][x] == 1:
                        mal[new_y][x].extend(mal[y][x][a:][::-1])
                    for j in mal[y][x][a:]:
                        pos[j] = [new_y, x, pos[j][2]]
                    if a != 0:
                        mal[y][x] = mal[y][x][:a]
                    else:
                        mal[y][x] = []
                else:
                    mal[new_y][x].append(i)
                    pos[i] = [new_y, x, d]
                    mal[y][x] = []
            else:
                d = 3
                new_y = y - 1
                if new_y <0 or board[new_y][x] == 2:
                    pos[i][2] = d
                else:
                    if len(mal[y][x]) > 1:
                        a = mal[y][x].index(i)
                        if board[new_y][x] == 0:
                            mal[new_y][x].extend(mal[y][x][a:])
                        elif board[new_y][x] == 1:
                            mal[new_y][x].extend(mal[y][x][a:][::-1])
                        for j in mal[y][x][a:]:
                            pos[j] = [new_y, x, pos[j][2]]
                        pos[i][2]=d
                        if a != 0:
                            mal[y][x] = mal[y][x][:a]
                        else:
                            mal[y][x] = []
                    else:
                        mal[new_y][x].append(i)
                        pos[i] = [new_y, x, d]
                        mal[y][x] = []
        for j in pos:
            if len(mal[j[0]][j[1]])>=4:
                flag=True
                break
        if flag:
            break
    #print(pos)
        '''for j in range(n):
            print(*mal[j])
        print('*'*20, answer,i)'''
    if flag:
        break
    answer+=1

if answer>1000:
    print(-1)
else:
    print(answer)