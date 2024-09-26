from collections import Counter
r,c,k=map(int,input().split())
board=[]
for _ in range(3):
    board.append(list(map(int,input().split())))

cnt=0
while cnt<=100:
    if r<=len(board) and c<=len(board[0]) and board[r - 1][c - 1] == k:
        break
    new_board = []
    if len(board)>=len(board[0]):

        max_len=0
        for i in range(len(board)):
            tmp=[]
            now=Counter(board[i])
            if 0 in now:
                now.pop(0)
            now=sorted(now.items(),key=lambda x:(x[1],x[0]))
            for j in now:
                tmp.append(j[0])
                tmp.append(j[1])
            new_board.append(tmp)
            max_len=max(len(new_board[i]),max_len)
            for j in range(len(new_board)):
                if len(new_board[j])<max_len:
                    new_board[j].extend([0]*(max_len-len(new_board[j])))
    else:
        max_len=0
        for i in range(len(board[0])):
            tmp = []
            for j in range(len(board)):
                tmp.append(board[j][i])
            now = Counter(tmp)
            if 0 in now:
                now.pop(0)
            now = sorted(now.items(), key=lambda x: (x[1],x[0]))
            im=[]
            for j in now:
                im.append(j[0])
                im.append(j[1])
            new_board.append(im)
            max_len = max(len(new_board[i]), max_len)
        for j in range(len(new_board)):
            if len(new_board[j]) < max_len:
                new_board[j].extend([0] * (max_len - len(new_board[j])))
        new_board=list(map(list,zip(*new_board)))

    board=new_board
    cnt+=1
if cnt>100:
    print(-1)
else:
    print(cnt)