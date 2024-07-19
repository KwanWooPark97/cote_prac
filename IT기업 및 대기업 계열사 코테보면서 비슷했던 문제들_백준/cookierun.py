n=int(input())

answer=[]

board=[list(input()) for i in range(n)]

def find_heart(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]=='*':
                return j,i+1

def find_left_arm(x,y):
    cnt=0
    for i in range(x-1,-1,-1):
        if board[y][i]=='_':
            return cnt
        else:
            cnt+=1
    else:
        return cnt

def find_right_arm(x,y):
    cnt=0
    for i in range(x+1,n):
        if board[y][i]=='_':
            return cnt
        else:
            cnt+=1
    else:
        return cnt

def find_mid(x,y):
    cnt=0
    for i in range(y+1,n):
        if board[i][x]=='_':
            return cnt
        else:
            cnt+=1
    else:
        return cnt

def find_left_leg(x,y):
    cnt=0
    for i in range(y,n):
        if board[i][x]=='_':
            return cnt
        else:
            cnt+=1
    else:
        return cnt
def find_right_leg(x,y):
    cnt=0
    for i in range(y,n):
        if board[i][x]=='_':
            return cnt
        else:
            cnt+=1
    else:
        return cnt
heart_x,heart_y=find_heart(board)
answer.append(find_left_arm(heart_x,heart_y))
answer.append(find_right_arm(heart_x,heart_y))
answer.append(find_mid(heart_x,heart_y))
answer.append(find_left_leg(heart_x-1,heart_y+answer[2]+1))
answer.append(find_right_leg(heart_x+1,heart_y+answer[2]+1))

print(f"{heart_y+1} {heart_x+1}")
for i in answer:
    print(i,end=' ')
